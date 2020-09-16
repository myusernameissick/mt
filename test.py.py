import discord
from discord.ext.commands import bot
emoji = '\N{THUMBS UP SIGN}'
client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()


    if message.content.startswith("hello"):
        await  message.channel.send("fuck you")

    if message.author == client.user:await message.add_reaction(emoji)

client.run('NzU1NDA5NjgyODg5NDQxMzAw.X2C4Fw.FHKAcL2pyhcQkSB3GNVKFomKGlw')
