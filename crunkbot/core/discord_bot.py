import discord

class DiscordBot(discord.Client):

    
    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return 
        
        print(f"Received message from: {message.author}")
        
        if message.content.startswith("$Hello"):
            await message.channel.send('Hello there!')

