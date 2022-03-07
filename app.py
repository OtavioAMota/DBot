import discord
import os
from dotenv import load_dotenv
import learningBot.learn_bot

learn_bot('intents.json')

load_dotenv()
TOKEN = os.getenv('TOKEN')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("Dbot"):
        response = chatbot.resquest(message.content[5:])
        await message.channel.send(response)

print("Bot running...")
client.run(TOKEN)
