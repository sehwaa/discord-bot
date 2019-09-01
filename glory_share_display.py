from discord.ext import commands
import discord
import random
 
token = 'Your Token'

bot = commands.Bot(command_prefix='$')
 
@bot.event
async def on_ready():
    print('logged in as \nname: {}\n  id: {}'.format(bot.user.name, bot.user.id))
    print('='*80)
    
    await bot.change_presence(game=discord.Game(name='화면공유', type=1))
 
@bot.command(pass_context=True)
async def share(ctx):
    voice_channel = ctx.message.author.voice.voice_channel

    voice_channel_id = voice_channel.id

    url = 'https://discordapp.com/channels/611294722501378048/'+str(voice_channel_id)

    await bot.say('{}'.format(url))