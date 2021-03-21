import discord
from chatterbot import ChatBot

bot = discord.Client(intents=discord.Intents.default())

chatbot = ChatBot('Unimportant Bot Name')


@bot.event
async def on_ready():
    print('Ready!')


@bot.event
async def on_message(message):
    if message.author != bot.user:
        print(message.content)
        channel_id = CHANNEL_ID_HERE
        if message.channel.id == channel_id:
            response = chatbot.get_response(message.content)
            print(response)
            await message.channel.send(response)


bot.run('TOKEN')
