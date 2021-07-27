# End to end encrypted chat via Discord


## Setup
To get started with this app, you will need to do a little bit of setup first.
These instructions are for Debian Linux. If anyone would like to add instructions for other operating systems, please do!


First, clone the repository and navigate to the project directory.
```
git clone https://github.com/zjtalia/discord_e2ee
cd discord_e2ee
```


Next, create a virtual environment for the app. Inside of the directory, run the command:
`python3 -m venv bot-env`

Activate the virtual environment:
`source bot-env/bin/activate`

Next, you will need to install the dependencies for the project. Run the following command:
`pip install -r requirements.txt`



Finally, you need to rename the file .env_placeholder to .env:
`mv .env_placeholder .env`

Next, open the file in your favorite text editor.
This file stores values that are private and cannot be included in the source code, or would be different depending on the user.
So far this file incudes the bot token and the discord channel id, but could include username, public/private keys, etc. in the future.

You can find the token on the bot's page at https://discord.com/developers/applications/. Click on the "Bot" tab, and then click copy. Paste the value after the equals sign on the line that says "DISCORD_TOKEN="

To find the channel id, make sure you have developer mode enabled on discord. Right click on the channel, and click "Copy ID". Paste the value after the equals sign on the line that says "CHANNEL_ID"

When you are done, your .env file should look like so:
```
# .env

# Provide the required values below

DISCORD_TOKEN=t0k3N.123
CHANNEL_ID=133742069
```


## Running the scripts

Now that setup is complete, here is how to use the scripts. Encryption has not been implemented yet, but you can currently use the scripts `send_message.py` and 'receive_message.py' to emulate the discord channel in the terminal.

First, navigate to the `scripts` directory
`cd scripts`

As it stands right now, these scripts need to run in separate terminal windows. Open up another terminal and navigate to the same directory. Then run `python3 receive_message.py` in one terminal, and `python3 send_message.py` in the other. I like to use a horizontally split terminal with 'receive_message.py' on top, and 'send_message.py' on the bottom.

## TO DO

* Allow the functionality of both scripts to operate in a single terminal instance, either via threading or the discord.py API wrapper (possibly using client.run()?)

* Develop and implement a cryptographic protocol

* Create a GUI 