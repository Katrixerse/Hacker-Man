import discord

client = discord.client

prefix = "?"

@client.event
async def on_ready():
    print('Ready!')
    
@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'ping'):
       await client.send_message(message.channel, 'Pong!')

client.run('token')
