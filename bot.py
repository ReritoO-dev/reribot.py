import discord

import asyncio





@bot.event

async def on_ready():

  return await bot.change_presence(activity=discord.Activity(type=1,name='r!yardım gibi komutlar yakında!', url='https://twitch.com/twitch'))

  print('bot is ready')

  

bot.run('Nzk1MzQ0ODI0OTY1OTIyODQ2.X_IAlw.9fdTnu7KA2YReDgfZb8kXACNMdw') 
