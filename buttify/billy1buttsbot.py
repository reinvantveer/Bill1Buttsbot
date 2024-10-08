from random import random

from twitchio import Message
from twitchio.ext import commands

from main import Settings


# Since the bot is untyped, we need to ignore the type check for the class
class Billy1ButtsBot(commands.Bot):  # type: ignore[misc]
    def __init__(self, settings: Settings, *args: list[str], **kwargs: dict[str, str]) -> None:
        super().__init__(*args, **kwargs)
        self.settings = settings

    async def event_message(self, message: Message) -> None:
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        if message.author.name in self.settings.ignore_users:
            return

        await self.handle_commands(message)

        roll = random()
        if roll < self.settings.chance:
            self.buttify(message)

    def buttify(self, message: Message) -> None:
        message.content = f"{message} butts"
