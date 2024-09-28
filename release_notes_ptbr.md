# ReleaseNotes

**v118 2024-08-11**
- Feat: For groups with the topics function, there is now the ability to download all files from a specific topic using `exec_downloadall.bat` and pasting the link of a message from the topic. It also works for groups with protected content.

**v117 2024-08-09**
- Fix: "KeyError file_name" error when executing clonechat_protect_dw.

**v116 2024-08-08**
- Fix: clonechat_protect_up was generating a "`json.decoder.JSONDecodeError`" when executing the show_history_overview function. Caused by the history being in the process of downloading. Now it emits a message to wait for the history download.

**v115 2024-07-18**
- Fix: clonechat_protect_up couldn't find the chat history file
- Fix: DownloadAll generating NotADirectoryError in chats with titles containing special characters

**v114 2024-07-16**
- Feat: clonechat_protect accepts channel or group identification by message link

**v113 2024-07-15**
- Fix: Chats with titles containing special characters no longer generate errors in the file system

**v112 2024-07-14**
- Refact: clonechat_protect with download pipeline separated from upload pipeline
- Feat: Execution scripts based on virtual environment. Script to create virtual environment (install.bat)