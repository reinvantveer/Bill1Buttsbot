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
    # A list of users to ignore.
    ignore_users: list[str]
    # The chance of buttification.
    chance: float
    # Whether to run in dry-run mode. Does not actually send messages if True.
    dry_run: bool
