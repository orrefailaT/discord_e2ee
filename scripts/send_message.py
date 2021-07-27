#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import requests
import json

# the following values are stored in the file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('CHANNEL_ID')

# set the url and headers for the POST request
baseURL = 'https://discordapp.com/api/channels/{}/messages'.format(CHANNEL)
headers = { 'Authorization':'Bot {}'.format(TOKEN),
			'User-Agent':'discord_e2ee_bot',
			'Content-Type':'application/json', }
	

# Await user input for messages to send
while True:
	os.system('clear') # If you are also running receive_message.py, you will see the message text in that terminal

	message = input('message: ') 
	
	POSTedJSON = json.dumps ( {'content':message} )

	r = requests.post(baseURL, headers = headers, data = POSTedJSON) 