#!/usr/bin/env python3

import os
from dotenv import load_dotenv

import discord


# The following values are stored in the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 
CHANNEL_ID = os.getenv('CHANNEL_ID')


client = discord.Client()

# This function runs when the script is executed, after the bot has successfully connected to the client
@client.event
async def on_ready():
  # Fetch the message history from the channel, and print the sender and text
  channel = await client.fetch_channel(CHANNEL_ID)
  async for message in channel.history(limit=50, oldest_first=True):
    username = message.author.display_name
    text = message.content

    print(username + ':\n'+ text + '\n')


# This function runs whenever a message is sent in the text channel
@client.event
async def on_message(message):
  # Print the message sender and text 
  text = message.author.display_name + ': \n' + message.content
  print(text + '\n')
 

client.run(TOKEN)