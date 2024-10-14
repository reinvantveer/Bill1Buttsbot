from random import random

from loguru import logger
from twitchio import Message
from twitchio.ext import commands

from buttify.settings import Settings


# Since the bot is untyped, we need to ignore the type check for the class
class Billy1ButtsBot(commands.Bot):  # type: ignore[misc]
    def __init__(self, settings: Settings) -> None:
        super().__init__(token=settings.token, prefix="", initial_channels=[settings.channel])
        self.settings = settings

        # Initialize the list of active chatters.
        self.active_chatters = set()

        # Validate the token: it should start with "oauth:"
        if not self.settings.token.startswith("oauth:"):
            raise ValueError(f"Token should start with 'oauth:', got: {self.settings.token}")

    async def event_ready(self) -> None:
        """Just a debug message to let us know that the bot is connected."""
        logger.info(f"Connected to {self.connected_channels} as {self.nick}")

    async def event_message(self, message: Message) -> None:
        logger.debug(f"Received message from {message.author.name}: {message.content}")
        # Messages with echo set to True are messages sent by the bot...
        # For now, we just want to ignore them...
        if message.echo:
            logger.debug(f"Ignoring echo message from {message.author.name}")
            return

        if message.author.name == self.settings.user:
            logger.debug(f"Ignoring message from self")
            return

        # Ignore messages from ignored users.
        if message.author.name in self.settings.ignore_users:
            logger.debug(f"Ignoring message from ignored user {message.author.name}")
            return

        # Ignore the first message from any user. This prevents new users from being buttified immediately.
        if message.author.name not in self.active_chatters:
            logger.debug(f"Ignoring first message from {message.author.name}")
            self.active_chatters.add(message.author.name)
            return

        roll = random()
        if roll < self.settings.chance:
            self.buttify(message)

        await self.handle_commands(message)

    def buttify(self, message: Message) -> None:
        message.content = f"{message} butts"
