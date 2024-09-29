from __future__ import annotations

import collections
import json
import time
from pathlib import Path
from time import sleep

import pyrogram
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn, FileSizeColumn

from ..utils.csv_util import open_csv, save_csv
from ..utils.timeout import time_out

console = Console()


def get_next_to_upload(cloneplan_path: Path, loop_seconds: int = 5) -> int:
    """returns the smallest message_id not yet cloned
    Message_id is authorized for cloning when its clone flag = "1"
    If all message_id have been cloned, returns value "0".
    If there are still message_id to be cloned but at the moment
    there are no authorized, make available available every x seconds.
    Args:
        cloneplan_path (Path): _description_

    Returns:
        int: message_id. 0 If there was no more messages to clone
    """

    while True:
        list_data = open_csv(cloneplan_path)
        dict_data = collections.OrderedDict(
            sorted({int(item["id"]): item for item in list_data}.items())
        )  # ordered from the smallest ID to the largest

        # Check if everything has been cloned. If yes, it returns zero
        clone_done = True
        for row_data in dict_data.values():
            if row_data["clone"] == "0":
                clone_done = False
                break
        if clone_done:
            return 0

        # If not, operate in loop looking for next message_id to be cloned
        for message_id in dict_data.keys():
            if (
                dict_data[message_id].get("download", "") == "1"
                and dict_data[message_id].get("clone", "") == "0"
            ):
                return message_id
        sleep(loop_seconds)


def get_caption(message_id: int, file_path_hist: Path) -> str:

    list_dict_msg = json.loads(open(file_path_hist, "r").read())
    caption = ""
    for dict_msg in list_dict_msg:
        if dict_msg["id"] == message_id:
            caption = dict_msg.get("caption", "")
            break
    return caption


def send_video(
    client_name: str,
    session_folder: Path,
    chat_id,
    file_path: Path,
    caption: str,
) -> Path:

    client = pyrogram.Client(client_name, workdir=session_folder)
    client.start()

    c_time = time.time()
    prefix = "UP"
    client.send_video(
        chat_id,
        file_path,
        caption=caption,
        progress=progress_bar,
        progress_args=(c_time, prefix),
        supports_streaming=True,
    )
    client.stop()
    return file_path


def send_document(
    client_name: str,
    session_folder: Path,
    chat_id: int,
    file_path: Path,
    caption: str,
) -> Path:

    client = pyrogram.Client(client_name, workdir=session_folder)
    client.start()

    c_time = time.time()
    client.send_document(
        chat_id,
        str(file_path),
        caption=caption,
        progress=progress_bar,
        progress_args=(c_time,),
    )
    client.stop()
    return file_path


def send_photo(
    client_name: str,
    session_folder: Path,
    chat_id: int,
    file_path: Path,
    caption: str,
) -> Path:

    client = pyrogram.Client(client_name, workdir=session_folder)
    client.start()

    client.send_photo(
        chat_id,
        str(file_path),
        caption=caption,
    )
    client.stop()
    return file_path


def send_audio(
    client_name: str,
    session_folder: Path,
    chat_id: int,
    file_path: Path,
    caption: str,
) -> Path:

    client = pyrogram.Client(client_name, workdir=session_folder)
    client.start()

    client.send_audio(
        chat_id,
        file_path,
        caption=caption,
    )
    client.stop()
    return file_path


def send_voice(
    client_name: str,
    session_folder: Path,
    chat_id: int,
    file_path: Path,
    caption: str,
) -> Path:

    client = pyrogram.Client(client_name, workdir=session_folder)
    client.start()

    client.send_voice(
        chat_id,
        file_path,
        caption=caption,
    )
    client.stop()
    return file_path


def get_sticker_id(message_id: int, file_path_hist: Path) -> str:

    list_dict_msg = json.loads(open(file_path_hist, "r").read())
    caption = ""
    for dict_msg in list_dict_msg:
        if dict_msg["id"] == message_id:
            caption = dict_msg["sticker"].get("file_id", "")
            break
    return caption


def send_sticker(
    client_name: str, session_folder: Path, chat_id: int, sticker_id: str
):

    client = pyrogram.Client(client_name, workdir=session_folder)
    client.start()

    client.send_sticker(
        chat_id,
        sticker=sticker_id,
    )
    client.stop()


def get_text(message_id: int, file_path_hist: Path) -> str:

    list_dict_msg = json.loads(open(file_path_hist, "r").read())
    caption = ""
    for dict_msg in list_dict_msg:
        if dict_msg["id"] == message_id:
            caption = dict_msg.get("text", "")
            break
    return caption


def send_message(
    client_name: str, session_folder: Path, chat_id: int, text: str
):
    def run_send_message(client_name, session_folder, chat_id, text):
        client = pyrogram.Client(client_name, workdir=session_folder)
        client.start()
        client.send_message(
            chat_id,
            text=text,
        )
        client.stop()

    try:
        run_send_message(client_name, session_folder, chat_id, text)
    except Exception as e:
        print(f"\n{client_name}-{e} \n Error. Retrying to send message")
        while True:
            try:
                run_send_message(client_name, session_folder, chat_id, text)
                break
            except Exception as e:
                sleep(5)
                print("...")


def upload_media(
    client_name: str,
    session_folder: Path,
    chat_id: int,
    message_id: int,
    cloneplan_path: Path,
    history_path: Path,
    auto_restart: int,
):
    list_data = open_csv(cloneplan_path)
    dict_data = collections.OrderedDict(
        sorted(
            {int(row_data["id"]): row_data for row_data in list_data}.items()
        )
    )
    message_type = dict_data[message_id]["type"]
    file_path = dict_data[message_id]["file_path"]
    caption = get_caption(message_id, history_path)
    console.print(f"[bold cyan]Uploading:[/bold cyan] {Path(file_path).name}")

    upload_function = None
    params = {
        "client_name": client_name,
        "session_folder": session_folder,
        "chat_id": chat_id,
    }

    if message_type == "video":
        upload_function = send_video
        params.update({"file_path": file_path, "caption": caption})
    elif message_type == "document":
        upload_function = send_document
        params.update({"file_path": file_path, "caption": caption})
    elif message_type == "photo":
        upload_function = send_photo
        params.update({"file_path": file_path, "caption": caption})
    elif message_type == "audio":
        upload_function = send_audio
        params.update({"file_path": file_path, "caption": caption})
    elif message_type == "voice":
        upload_function = send_voice
        params.update({"file_path": file_path, "caption": caption})
    elif message_type == "sticker":
        sticker_id = get_sticker_id(message_id, history_path)
        upload_function = send_sticker
        params["sticker_id"] = sticker_id
    elif message_type == "text":
        text = get_text(message_id, history_path)
        upload_function = send_message
        params["text"] = text

    if upload_function:
        time_out(
            auto_restart * 60,
            upload_function,
            params,
            True,
        )
    console.print()


def set_clone(cloneplan_path: Path, message_id: int):

    list_data = open_csv(cloneplan_path)
    for data in list_data:
        if data["id"] == str(message_id):
            data["clone"] = 1
            break
    save_csv(list_data, cloneplan_path)


def delete_local_media(cloneplan_path: Path, message_id: int):

    list_data = open_csv(cloneplan_path)
    dict_data = collections.OrderedDict(
        sorted(
            {int(row_data["id"]): row_data for row_data in list_data}.items()
        )
    )
    file_path = dict_data[message_id]["file_path"]
    if Path(file_path).exists() and file_path != "":
        Path(file_path).unlink()


def pipe_upload(
    client_name: str,
    session_folder: Path,
    chat_id: int,
    cloneplan_path: Path,
    history_path: Path,
    auto_restart: int = 20,
):
    console.print("[bold green]Starting media upload...[/bold green]")
    message_id = None
    while message_id != 0:
        message_id = get_next_to_upload(cloneplan_path)
        if message_id == 0:
            console.print("[bold green]Everything was uploaded :)[/bold green]")
            return

        upload_media(
            client_name,
            session_folder,
            chat_id,
            message_id,
            cloneplan_path,
            history_path,
            auto_restart,
        )
        set_clone(cloneplan_path, message_id)
        delete_local_media(cloneplan_path, message_id)

    console.print("[bold green]All uploads completed successfully![/bold green]")


def progress_bar(current, total, c_time, prefix=""):
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        "•",
        FileSizeColumn(),
        "•",
        TimeRemainingColumn(),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task(f"[cyan]{prefix} Uploading", total=total)
        while not progress.finished:
            progress.update(task, completed=current)
            if current >= total:
                break
            time.sleep(0.1)