"""A tiny bot with the VR status. Run it with:  DISCORD_TOKEN=your-token python example.py"""

import os

import discord

from vr_status import show_vr_status

bot = discord.Client(intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}. Open its profile in Discord to see the VR headset.')


show_vr_status()
bot.run(os.environ['DISCORD_TOKEN'])
