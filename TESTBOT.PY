import discord
from discord import player
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.ext.commands.core import command
from discord import FFmpegPCMAudio


TOKEN = 'OTIxMjYyMzgwNTIzMDk0MDY3.YbwWcw.MlPSvR9hRCyIHzxtyYuqpI98Uqw'

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print("bot online")

@client.command(pass_context= True)
async def join(ctx):
    if (ctx.author.voice):
        channel =  ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('test.mp3')
        player = voice.play(source)
        
    else:
        await ctx.send("You are not in a voice channel!")

@client.command(pass_context= True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel!")
    else:
        await ctx.send("I am not in a voice channel!")

client.run(TOKEN)            