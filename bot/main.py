import logging
import json
import os

# which discord library???
# Nextcord seems good, so using that
# https://docs.nextcord.dev/en/stable/index.html

import nextcord
from nextcord.ext import commands

base_location = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(f"{base_location}/config.json"):
    print("Config file doesn't exist, creating file")
    config = {}
    config["token"] = input("Bot token: ")
    config["bot_name"] = input("Bot name: ")
    config["description"] = input("Short description: ")
    config["settings"]["some_setting"] = False
    config["settings"]["log_level"] = "CRITICAL"    

with open(f"{base_location}/config.json", "r") as f:
    config = json.load(f)

# https://docs.nextcord.dev/en/stable/logging.html
logging.basicConfig(level=logging.INFO)



bot = commands.Bot()

@bot.event
async def on_ready():
    print("Bot started...")
    print(f"Logged in as {bot.user}")

@bot.slash_command(name="test", description="Test slash")
async def test_slash(interaction: nextcord.Interaction):
    await interaction.send("HEllo!")




# Loading cogs



bot.run(config["token"])