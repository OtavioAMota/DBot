import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
print("bot learning...")
chatbot.tran_model()
chatbot.save_model()
client = discord.Client()

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
