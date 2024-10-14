from dataclasses import dataclass


@dataclass
class Settings:
    """A dataclass to hold the settings for the bot."""
    # The twitch channel to connect to.
    channel: str
    # The user that will operate the bot.
    user: str
    # The OAuth token for the bot.
    token: str
    ignore_users: list[str]
    chance: float