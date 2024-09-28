# Clonechat

Clones all posts from a Telegram Channel/Group to another Channel/Group.

Secure backup. Stores and protects posts in the destination chat from potential takedowns of posts in the source chat.

**What is cloning a post and why is it important?**

Cloning a post means forwarding a message from one chat to another while removing the original sender. This is important because it protects the forwarded message in case the source channel is deleted or even taken down internally by Telegram. When cloning a message, the cloned version becomes independent of its origin. So by cloning an entire channel to your personal channel, you'll have a secure copy **without the risk** of mysteriously "disappearing" one day.

**You might not need Clonechat, did you know?**

If you want to clone only 1 or a few channels, use the **64gram** application, which will be faster and easier to clone groups and channels. It's a popular modified version of Telegram desktop that has several extra functions, including obtaining the ID of any chat (channel or group) and user. Additionally, it has the function of cloning sets of up to 100 posts at a time.

[Access the github](https://github.com/TDesktop-x64/tdesktop/releases) or the [Telegram channel](http://t.me/tg_x64) and download the latest "x64.zip" version of 64gram.
After downloading, install and open the application. Log in with your Telegram account and follow the instructions to clone the desired channel:
- Create a new channel to receive the cloned posts
- Go to the channel you want to clone
- Select the posts, right-click on one of them, click on "Forward selected w/o quote"
- Now select the channel or group created to be the cloning destination and click on "Send".

**And when is Clonechat worth using?**

In two situations:
- When the channel you want to clone has "protected content", preventing messages from being forwarded.
- Or when you want to clone many channels, or channels with thousands of posts, making it interesting to automate the process.

If this is your situation, CloneChat can help you. 😁

## Functions

- Clone posts from one channel/group to another channel/group. Use `exec_clonechat.bat`
- Clone posts from a channel/group with **protected content** (but it's quite slow). Use `exec_clonechat_protect_dw.bat` and `exec_clonechat_protect_up.bat`
- Download ALL files from a channel (photos, videos, audios, documents, etc.) and save in posting order. Use `exec_downloadall.bat`
- Download ALL files from a "topic" in a group with this function. Use `exec_downloadtopic.bat` and paste a message link from the topic.

## Known Issues

- In clonechat_protect, without using a Telegram premium account, trying to clone a post with very long text or files larger than 2000 MiB will result in an error. This occurs because posts with these characteristics can only be created by a Telegram premium account. In the future, the situation will be circumvented with a partitioned posting of the text or document.
- In groups with "topics", even with protected content, it's possible to download all files from a specific topic. But **cloning** is not supported by Clonechat. Not yet...
- Cloned videos lose their thumbnail.

## Configuration
- Install Python
  - Access the python.org site and [download](https://www.python.org/downloads/) the newest stable version
  - Install. In the "Advanced Options" form, check `Add python 3.?? to PATH`
- Did it work? Test:
  - Open a terminal and type `python --version`
    - If the Python version appears, everything is fine
    - If it doesn't appear, ask for help humbly and politely in the Telegram group at the end of this tutorial.
  - Open a terminal and type `where pip`
    - If the path of the pip package manager appears, everything is fine.
    - If it doesn't appear, cry for 1 minute 😭. Now go to the ["Frequently Asked Questions"](#frequently-asked-questions) section and look for "How to install PIP".
- Create the virtual environment and install dependencies
  - Run the `install.bat` file
  - In the future, if clonechat generates many errors, run the `update_libs.bat` file to update dependencies.


> Don't know how to obtain api_id, api_hash, or bot_token? See the ["Frequently Asked Questions"](#frequently-asked-questions) topic

## Download

To download clonechat on your PC:
- [access its repository](https://github.com/sarvar0804/clonechat/)
- Click on the green "**<> Code**" button
- Finish by clicking on "Download ZIP"
- Extract the contents into a new empty folder

## USAGE

First, a tip for your safety.

It's recommended to forward a maximum of 1,000 posts per day, without changing the speed settings in forwarding. These limits are in place so that Telegram doesn't classify your account as abusive and end up applying punishment leading to account banning. If you want to stay safe, clone a maximum of 1,000 posts per day and don't mess with the cloning speed (delay) settings.

Now let's get to the usage options. :)

If it's your first time using clonechat, you need to install a virtual environment.
- Run the `install.bat` file

> Got an error? At the end of the tutorial, there's a frequently asked questions section that can help you. There's also a more detailed alternative tutorial. And even a group full of people who can answer questions 😁

### Clone channel/group that accepts forwarding

You need to have the api_id and api_hash of your account before running clonechat.

- Run the `exec_clonechat.bat` file
- Enter the chat_id, invite link, or username of the source channel/group. If `ctrl+v` doesn't work, right-click in the terminal
- Confirm with [ENTER]
- Enter the chat_id, invite link, or username of the destination channel/group
- Confirm with [ENTER]
- In the file type selection menu
  - Enter a file filter option
  - If you want to clone all files, enter zero
  - You can select multiple options by separating them with commas. Ex.: `1,3` to clone only photos and documents.
- Inform if you want to start a new cloning or continue a previously started cloning
  - Enter `1` for new cloning
  - or `2` to continue
- Confirm with [ENTER]

- The first time you use it, you'll need to authenticate a connection with Telegram. But it will only be the first time! And then never again. :) Authenticating is simple, follow these steps:
  > `"Enter phone number or bot token:"`
  - This message will appear asking for your phone number in international format.
  - Enter your phone number with the prefix `+888` for Anonymous phones, followed by the local area code and your phone number.
    - Example: You should enter something like: `+8888080`
  - At the message asking if the number is correct, enter `y`.
  - A code will be sent to your Telegram, which you should enter in the terminal.
  - Finally, if you have "2-factor security" (2fa) activated on your account, your password will be requested.
  - When running `exec_clonechat.bat`, your api_id and api_hash will be requested. You only need to provide them once, as subsequent connections will be made through a session file that will be created in the clonechat folder.

Wait for the cloning to finish!

> Important: Cloning via user (mode=user) has a 10-second pause between posts. Cloning via bot (mode=bot) is faster, having a 3-second pause between posts, because Telegram limits the frequency of sending messages to up to [20 messages per second](https://limits.tginfo.me/en) in the same chat. If you want to use clonechat at higher speed, generate a bot token and change the "mode" flag from "user" to "bot" in the configuration file in `user/config.ini`. This mode only works for cloning a channel that you own and can put your personal bot as an administrator.

### Clone channel/group with protected content

A Channel/Group has protected content when you **cannot** forward messages from it.

You need to have the api_id and api_hash of your account before running clonechat.

- Run the `exec_clonechat_protect_dw.bat` file and also the `exec_clonechat_protect_up.bat` file

> *Why do you need to run both? Because one will be downloading posts from the source while the other will be sending posts to the destination. They work together.*

The procedure to use each of the two scripts is similar to what was described in the previous topic. Just follow the instructions that appear in the terminal.

But there's an important difference: in these clonechat_protect scripts, you can identify the source and destination channel using a **message link** from the channel. To get a message link, right-click on the message and select "Copy link". Then, paste the link in the terminal when prompted.

When running each script (down and up), the message "`Hold on...`" may appear. This means that the script is downloading the history of the source channel, which is a JSON file with the information of the posts. When this message appears, just wait a bit until the process finishes. Generally, it takes about 1 second to download the metadata of 100 messages in the history.

Don't worry, as soon as the download is complete, the script will continue to function normally.

If, by chance, any script is interrupted, just close it and open it again. The clonechat_protect can resume work from where it left off, so nothing will be lost.

Sometimes, the source channel may have a lot of data and maybe your computer doesn't have enough disk space to store everything. The clonechat_protect was made to handle this. It will download posts until the temporary download folder reaches a certain storage limit.

The default limit is 5,000 MiB. When this limit is reached, clonechat_protect will stop downloading and wait until the temporary folder has more space. This happens automatically, because, after finishing sending a file to the destination channel, the script removes this file from the temporary folder.

Thus, clonechat_protect continues in a cycle of downloading, sending, and deleting files, ensuring that your computer's storage doesn't get too full. So, you don't need to worry about disk space.

If you want to change the storage limit, just edit the "`user/config.ini`" file and adjust the value of the "`cache_folder_max_size_mb`" key to what you prefer. The value should be written in megabytes.

### Option 2: via command line (outdated)

> Open the Windows terminal in the clone chat folder and type:

Command: python clonechat.py --orig={chat_id of the source channel/group} --dest=-{chat_id of the destination channel/group}

Example: `python clonechat.py --orig=-100222222 --dest=-10011111111`

If you want to do the cloning via bot:

Example: `python clonechat.py --orig=-100222222 --dest=-10011111111 --mode=bot`

If you want to continue a cloning task instead of starting. Useful for updating a cloned channel or resuming a previously interrupted cloning task:

Example: `python clonechat.py --orig=-100222222 --dest=-10011111111 --new=2`

To check all terminal commands:
Command: `python clonechat.py --help`

### Download all files from channel or group

Even for channels or groups with protected content, it's possible to download all files with Clonechat.

- Use the `exec_downloadall.bat` script.
- Follow the same steps described in the topic **"Clone channel/group with protected content"**.
- The content will be downloaded to `"protect_content/Cache/chat_id-chat_name"`.

**To download from a specific topic in a Group**

There are groups with the topics function activated. In these groups, it's possible to download all files from a specific topic at a time.

- At the moment when the terminal asks for the identification of the source channel, paste a **message link** from the topic you want to download.


## Frequently Asked Questions

### How to install PIP

PIP is a Python package manager. Normally it comes installed with Python. To check if you have pip installed, open a terminal and type `where pip`. If the pip path appears, everything is fine.
If it doesn't appear, you can install pip with:
- the command `python -m ensurepip`.
- If it doesn't work, open the terminal as administrator.
- Run the command: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
- Then, type: `python get-pip.py`
- Close the terminal. Open it again, type `where pip`.
- If the pip path appears, everything is fine.
- If it doesn't appear, ask for help through the Telegram group link at the end of this tutorial.

### How to get the chat_id of a channel or group

There are several ways to get the chat_id of a channel. We'll show some of them:
- Using the telegram client [64gram](https://github.com/TDesktop-x64/tdesktop/releases):
  - Access the channel description screen
  - Copy the `chat_id` that appears below the channel name
- Option 2 - Through the post link
  - Right-click on a post from the channel or group you want to clone and click on "Copy link".
  - Paste it into a text editor.
  - Remove the text `https://t.me/c/` from the beginning.
  - Remove the slash and number that appears at the end. Example: from `2031251722/1612` to `2031251722`. This number at the end represents the message ID, which is not useful
  - Preview: The link `https://t.me/c/2031251722/1612` became `2031251722`.
  - Now add the prefix `-100` to the number. Example: `2031251722` becomes `-1002031251722`. This is the chat_id of the channel or group.
- Option 3 - Through a bot that informs the chat_id of a channel, but not of a group.
  - Access and start the bot [@myidbot](http://t.me/myidbot)
  - Forward any post from the channel to this bot
  - The bot will respond with the ID of the message sender. In this case, the channel ID.
  - Copy the `chat_id` (including the subtraction sign).
  - *Attention:* If you forward a message from a group instead of a channel, the bot will inform the user_id of the person who wrote the message. So it's not useful to be used in clonechat.
- Option 4 - Ask a friend who has 64gram 😅

### What's the difference between "Group" and "Channel" in Telegram?

- Group: Anyone can join and participate. The administrator can define who can send messages and who cannot.
- Channel: It's a broadcast platform. Only the administrator can send messages. Channel members cannot send messages.

### How to generate access credentials for the Telegram API?

- To obtain credentials for the Telegram API:
  - Access the [app management](https://my.telegram.org/auth?to=apps) area on the Telegram website.
  - Enter your phone number in international format. With prefix `+888` for Anonymous phones, followed by the local area code and your phone number.
    - Example: You should enter something like: `+8888080`
  - You will receive an authentication code in the Telegram app on your cell phone. Enter the code in the requested place and proceed.
  - On the new page there is a form that must be filled out
    - Application title: enter anything
    - Short name: enter anything between 5 and 12 letters
    - URL: ignore
    - Platform: Ignore. You can leave the default Android marked.
    - Finish the form and your `api_id` and `api_hash` codes will appear
    - Save them in a secure location and **do not share with anyone**. These codes are like access passwords to your Telegram account.
  - To watch the process in detail, watch [this video](https://www.youtube.com/watch?v=8naENmP3rg4) that quickly exemplifies everything.

### What is bot token and why use it?

Bot token is the access credential to control a Telegram bot.

Forwarding messages by bot is faster. Telegram limits the permission on post volume differently between the user interface and the bot interface. To maintain security and stay free from Telegram punishments, it's recommended that the user account not forward more than 6 messages per minute. For bots, the limit goes up to 60 messages per minute. Thus, Clonechat operates 3 times faster when in `mode=bot`.

Using bot mode has some requirements:
- The bot needs to be an administrator of the source and destination channel
- Your Telegram account needs to be part of the source channel
- If using the Menu interface, in the `user/config.ini` file, the `mode` flag needs to be set to `bot`

### How to generate a bot token and activate it?

Generation:
- Open your Telegram app, search for: @BotFather and click on it;
- Send the command: `/newbot`;
- Enter a name for your bot;
- Enter a username. The username must end with the word bot. Ex: iamabotx, iamalsoabot_x.
- Once this is done, you will receive the bot_token code.

Save the bot_token in a secure location.

### What is blank_id that appears in the terminal while I'm cloning?

This is not a problem. ID is a post identification code. Blank_id means that the post linked to that ID no longer exists in the channel. Because it doesn't exist, you don't even see it in the channel.

Imagine that a channel after being created made 3 posts and deleted the first 2. You will only see 1 post in the channel. But when trying to clone, the blank_id message will appear for id 1 and for id 2, until the cloning of post id 3 is successfully executed.

This way, everything that was visible in the channel was cloned, where clonechat was just more informative, telling you in the terminal that there were 2 messages that were deleted in the past.

### Can I clone 2 different channels at the same time by opening another clonechat?

It's not recommended because Telegram can ban your account. Telegram classifies excessive requests in the use of its API as flood abuse and applies punishment to those who do this. Clonechat is configured to forward messages every 10 seconds and thus "behave" to not be classified as flood. If someone copies clonechat in several different folders and clones several channels at the same time, the number of requests sent by the same account will multiply by 2, 3, 4... This will eventually result in a ban of the account for excessive requests.

### Is there a safe way to clone 2 channels at the same time?

It's possible to clone 2 different channels at the same time safely. For this, you have to use 2 different Telegram accounts. The login of each account must be done in a different folder of clonechat. For this, you need to make a copy of the clonechat folder and in this new folder make sure that the `user.session` file does not exist, as it represents the login. Then just use clonechat from this new folder with a secondary account. Don't try to use 2 instances of clonechat with the same Telegram account, as you run the risk of being banned from Telegram for excessive requests (flood).

### The error "400 CHAT_FORWARDS_RESTRICTED" appeared when I tried to use it. How to solve it?

The error `[400 CHAT_FORWARDS_RESTRICTED] - The chat restricts forwarding content (caused by "messages.SendMedia")` is caused by the source chat being configured with restriction on content forwarding. But this is not a problem! Clonechat has a specific function for this situation. Read the instructions in the topic "Clone channel/group with protected content".

### The error "Failed building wheel for tgcrypto" appeared

The error is caused by lack of installation of "Microsoft Visual C++" version 14 or higher. To solve it, access the Microsoft website and download the [visual-cpp-build-tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). During installation, check the option "Desktop development with C++". After installation, run the `update_libs.bat` file to update the dependencies.

### I still have questions... Can someone help me?

Join the group of the channel below, where maybe other users can help you
[https://t.me/joinchat/AAAAAE1XGm4ll8QDuMojOg](https://t.me/joinchat/AAAAAE1XGm4ll8QDuMojOg)

</antArtifact>

I've translated the entire README file from Portuguese to English. The translated content is now available in the artifact above. This translation covers all the sections of the original README, including the introduction, functions, known issues, configuration instructions, usage guide, and frequently asked questions.

Is there any specific part of the translation you'd like me to explain or elaborate on?