import discord
import asyncio

client = discord.client

prefix = "?"

@client.event
async def on_ready():
    print('Ready!')
    await client.change_presence(game=discord.Game(name='Some game'))
    
@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'ping'):
       await client.send_message(message.channel, 'Pong!')
    
    if message.content.startswith(prefix + 'prefix'):
       await client.send_message(message.channel, 'Current prefix is: ' + prefix)
    
    if message.content.startswith(prefix + 'flipcoin'):
       cointoflip = random.choice({"Heads!", "Tails!"})
       await client.send_message(message.channel, 'The coin has been flipped and landed on' + cointoflip)
        
    if message.content.startswith(prefix + '8ball'):
       async def echo(*, message: str):
       8ballresponse = random.choice({"It is certain.", "No doubt about it.", "No chance."})
         embed=discord.Embed()
         embed.add_field(name=You asked:, value=message, inline=False)
         embed.add_field(name=8ball says:, value=8ballresponse, inline=False)
       await client.say(embed=embed)
        
client.run('token')
