import discord
import os 
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import numpy as np


client = discord.Client()

animal = open('monkey.txt', encoding = 'utf8').read()
sentence = animal.split()

def make_pairs(sentence):
    for i in range(len(sentence)-1):
        yield (sentence[i], sentence[i+1])

pairs = make_pairs(sentence)
word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

monkey_words = ["monkey", "ape", "baboon", "gorilla", "primate", "orangutan", "chimp", "lemur", "macaque", "bonobo", "tamarin", "gibbon", "tarsier", "potassium"]
starter_monkey_responses = ["OOO OOO AA AA", "My man", "oooh yeah baby!!", "mreooowo", "MROOOOOWWW", "I AM MONKEY!", "GROROOOWLLLL", ":monkey:", ":see_no_evil:", ":hear_no_evil:", ":speak_no_evil:", ":banana:", "https://tenor.com/view/monkey-dizzy-gif-8071936", "https://tenor.com/view/talisman-monkeyemote-monkey-gif-15318336", "https://tenor.com/view/frozen-monkey-gif-4932553", "https://tenor.com/view/monkey-sleep-cute-monkey-monkey-reaction-sleeping-zzsoobn-gif-23386436", "https://tenor.com/view/monkey-bath-time-animal-cute-baby-monkey-gif-17531929", "https://tenor.com/view/monkey-angry-cute-face-cute-ugly-monkey-gif-13664907", "https://tenor.com/view/monkey-running-cute-monkey-monkey-singe-gif-24670782", "https://tenor.com/view/balenciagaval-monkey-eating-apple-gif-23099760", "https://tenor.com/view/monkey-dance-music-gif-19917522", "https://tenor.com/view/run-monkey-baby-monkey-cute-adorable-gif-17081972", "https://tenor.com/view/monke-feast-monkey-belly-cute-gif-21196848", "https://tenor.com/view/monkey-monkey-scared-scream-gif-17330983", "https://tenor.com/view/monkey-kiss-gif-10985520"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n -Wise Former Monkey"
  return(quote)

def update_responses(monkey_message):
  if "word" in db.keys():
    word = db["word"]
    word.append(monkey_message)
    db["word"] = word

  else:
    db["word"] = [monkey_message]

def delete_response(index):
  word = db["word"]
  if len(word) >index:
    del word[index]
    db["word"] = word

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  msg = message.content
  
  if message.author == client.user:
    return
    
  if message.content.startswith('hello monkey'):
    await message.channel.send("OOO OOO AA AA")

  if message.content.lower().startswith('banana'):
    await message.channel.send("omgomgomg do you have a bananananaanana")
    
  if msg.startswith('$wise') or msg.lower().startswith('wise monkey'):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_monkey_responses
  if "word" in db.keys():
    options += db["word"]
    
  if any(word in message.content.lower() for word in monkey_words):
    await message.channel.send(random.choice(starter_monkey_responses))
    
  if msg.startswith('$new'):
    new_message = msg.split("$new ", 1)[1]
    update_responses(new_message)
    await message.channel.send("New monkey response added!")

  if msg.startswith('$del'):
    word = []
    if "word" in db.keys():
        index =  int(msg.split("$del", 1)[1])
        delete_response(index)
        word = db["word"]
    await message.channel.send(word)

  speak_words = ["speak"]
  if any(word in message.content.lower() for word in speak_words):
    first_word = np.random.choice(sentence)
    while first_word.islower():
        first_word = np.random.choice(sentence)
    
    chain = [first_word]
    
    n_words = 20
    for i in range(n_words):
      chain.append(np.random.choice(word_dict[chain[-1]]))

    ' '.join(chain)
    good_sentence = ""
    for i in range(n_words):
      good_sentence += chain[i] + " "
      if chain[i][-1] in ".!?":
        break
    await message.channel.send(good_sentence)
  strawberry_words = ["strawberry", "strawberries"]
  strawberry_responses = ["YESS!!!!! :strawberry: :strawberry:", "https://tenor.com/view/monkey-monkey-eating-monkey-eating-strawberries-kardie-gif-gif-22488578", "https://tenor.com/view/tayomaki-monkey-strawberry-sakigifs-gif-22300171", "https://tenor.com/view/sushichaeng-monkey-eating-monkey-gif-20975604"]
  if  any(word in message.content.lower() for word in strawberry_words):
    await message.channel.send(random.choice(strawberry_responses))
  

  banana_words = ["banana"]
  banana_responses = ["gimme gimme gimme gimmme :banana: :banana:", ":banana:", "om nom nom nom", "\<snatches banana\>", "dont mind if i do", "\<stomach growl\>", "https://tenor.com/view/monkey-banana-give-me-dem-bananas-gif-15221350", "https://tenor.com/view/big-bite-monkeyboo-eat-hungry-yummy-gif-19333905", "https://tenor.com/view/snack-bananas-monkeys-cats-gif-21055918", "https://tenor.com/view/monkey-shocked-surprised-bananas-oh-yes-gif-15688672", "https://tenor.com/view/fast-monkey-banana-eat-funny-gif-20647740", "https://tenor.com/view/monkey-banana-gif-7848605", "https://tenor.com/view/cat-monkey-banana-eating-sad-gif-6230069"]
  if msg.lower().startswith("do you want a banana") or any(word in message.content.lower() for word in banana_words):
    await message.channel.send(random.choice(banana_responses))

  icecream_words = ["ice cream"]
  icecream_responses = ["nice cold treat for one HOT monkey", "https://tenor.com/view/monkey-ice-cream-licking-gif-23851733", "https://tenor.com/view/monkey-ice-cream-chew-yummy-gif-22780949", "https://tenor.com/view/thank-you-baby-monkey-ice-cream-gif-12873648", "YOU GONNA GIVE IT TO ME OR NOT", "https://tenor.com/view/monkeys-ice-cream-hungry-snacks-gif-3376935", "https://tenor.com/view/monkey-puppet-monkey-sidekick-monkey-stupid-gif-14891459", "https://tenor.com/view/monkey-lick-monkey-lick-tongue-cute-gif-13961187"]
  if msg.lower().startswith("do you want ice cream") or any(word in message.content.lower() for word in icecream_words):
    await message.channel.send(random.choice(icecream_responses))
  


keep_alive()
client.run(os.environ['token'])

