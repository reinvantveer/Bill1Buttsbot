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

        if message.author.name == self.settings.user and not self.settings.dry_run:
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
        """Buttify the message and send it back to the channel."""
        # Modify the message content. Split the message into words, and replace part of a random word with "butt".
        words = message.content.split()
        # Choose a random word from the message.
        word_index = int(random() * len(words))
        word = words[word_index]
        # Choose a random index in the word.
        char_index = int(random() * len(word))
        # Choose a maximum of 4 characters to replace.
        max_4_length = int(random() * 4)
        # Replace a random set of max 4 characters in the word with "butt".
        words[word_index] = word[:char_index] + "butt" + word[char_index + max_4_length:]

        # Emit the message back to the channel.
        if not self.settings.dry_run:
            self.connected_channels[0].send(' '.join(words))
        else:
            logger.info(f"Would have sent: {' '.join(words)}")