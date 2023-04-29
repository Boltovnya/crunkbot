from crunkbot.core.discord_bot import DiscordBot
from crunkbot.core.config import Config
import typing as t
from discord import Intents
import os


class Crunkbot():
    def __init__(self):
        self.config: dict = self.load_config()
    
    def load_config(self) -> dict:
        conf = Config("./")
        conf.from_env()
        return conf.config

    
    
    def run(self) -> bool:
        intents = Intents.default()
        intents.message_content = True

        client = DiscordBot(intents = intents)
        client.run(self.config["discord"]["bot_token"])
        return True

