from crunkbot.core.discord_bot import DiscordBot
import typing as t
from discord import Intents
import os


class Crunkbot():
    def __init__(self):
        self.check_env()
    
    def check_env(self) -> bool:
        env = os.environ.get("CBKEY")
        if not env:
            raise RuntimeError("m8 try again")
        self.run(env)
        return True
    
    
    def run(self, key: str, config: t.Optional[str] = None) -> bool:
        intents = Intents.default()
        intents.message_content = True

        client = DiscordBot(intents = intents)
        client.run(key)
        return True

