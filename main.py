import discord
import os 
import requests
import json
import random
from replit import db

client = discord.Client()
monkey_words = ["monkey", "ape", "baboon", "gorilla", "primate", "orangutan", "chimp", "lemur", "macaque", "bonobo", "tamarin", "gibbon", "tarsier"]
starter_monkey_responses = ["OOO OOO AA AA", "My man", "oooh yeah baby!!", "mreooowo", "MROOOOOWWW", "I AM MONKEY!", "GROROOOWLLLL"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n -Wise Former Monkey"
  return(quote)

def update_responses(monkey_message):
  if "monk" in db.keys():
    monk = db["monk"]
    monk.append(monkey_message)
    db["monk"] = monk

  else:
    db["monk"] = [monkey_message]

def delete_response(index):
  monk = db["monk"]
  if len(monk) >index:
    del monk[index]
    db["monk"] = monk

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  msg = message.content
  
  if message.author == client.user:
    return
    
  if message.content.startswith('$hello'):
    await message.channel.send("OOO OOO AA AA")

  if message.content.startswith('banana'):
    await message.channel.send("omgomgomg do you have a bananananaanana")
    
  if msg.startswith('$wise'):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_monkey_responses
  if "monk" in db.keys():
    options += db["monk"]
    
  if any(word in msg for word in monkey_words):
    await message.channel.send(random.choice(starter_monkey_responses))
    
  if msg.startswith('$new'):
    new_message = msg.split("$new ", 1)[1]
    update_responses(new_message)
    await message.channel.send("New monkey response added!")

  if msg.startswith('$del'):
    monk = []
    if "monk" in db.keys():
        index =  int(msg.split("$del", 1)[1])
        delete_response(index)
        monk = db["monk"]
    await message.channel.send(monk)

client.run(os.environ['token'])

