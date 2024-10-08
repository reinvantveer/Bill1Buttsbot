import argparse
import tomllib
from argparse import Namespace
from dataclasses import dataclass

from buttify.billy1buttsbot import Billy1ButtsBot


@dataclass
class Settings:
    channel: str
    user: str
    token: str
    ignore_users: list[str]
    chance: float


def main(args: Namespace) -> None:
    with open(args.config, "rb") as f:
        data = tomllib.load(f)

    settings = Settings(
        channel=str(data["billy1buttsbot"]["channel"]),
        user=args.user,
        token=args.token,
        ignore_users=list(data["billy1buttsbot"]["ignore_users"]),
        chance=float(data["billy1buttsbot"]["chance_of_buttification"]),
    )

    bot = Billy1ButtsBot(settings)
    bot.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Billy1ButtsBot service')
    parser.add_argument('--config', default='pyproject.toml', help='Configuration')
    parser.add_argument('--user', default='billy1buttsbot', help='User')
    parser.add_argument('--token', help='Twitch OAuth token', required=True)

    args = parser.parse_args()
    main(args)
