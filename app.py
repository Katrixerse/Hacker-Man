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
    
    if message.content.startswith(prefix + 'prefix'):
       await client.send_message(message.channel, 'Current prefix is: ' + prefix)
    
    if message.content.startswith(prefix + 'flipcoin'):
       cointoflip = random.choice({"Heads!", "Tails!"})
       await client.send_message(message.channel, 'The coin has been flipped and landed on' + cointoflip)

client.run('token')
