#!/usr/bin/env python3

import os
import sys

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# token value is stored in a file .env, which is not included in the source code
# a template version of this file can be provided when the app is ready for deployment


client = discord.Client()


@client.event
async def on_ready():
  print(f'{client.user} has connected to the Discord!')
  #any other operations to run on connection go here


@client.event
async def on_message(message):
  if message.author != client.user: #change this depending on whether there is one bot, or a bot for each user
    
    #example message response
    response = 'Received message: "' + message.content + '".'
    await message.channel.send(response)
 

client.run(TOKEN)
