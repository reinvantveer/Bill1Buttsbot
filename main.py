import argparse
import tomllib
from argparse import Namespace

from loguru import logger

from buttify.billy1buttsbot import Billy1ButtsBot
from buttify.settings import Settings


def main(args: Namespace) -> None:
    with open(args.config, "rb") as f:
        config = tomllib.load(f)["tool"]["billy1buttsbot"]

    settings = Settings(
        channel=str(config["channel"]),
        user=config["username"],
        token=args.token,
        ignore_users=list(config["ignore_users"]),
        chance=float(config["chance_of_buttification"]),
    )

    bot = Billy1ButtsBot(settings)
    logger.info("Starting Billy1ButtsBot... press Ctrl+C to stop.")
    bot.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Billy1ButtsBot service')
    parser.add_argument('--config', default='pyproject.toml', help='Configuration')
    parser.add_argument('--token', help='Twitch OAuth token, see https://twitchapps.com/tmi/', required=True)

    args = parser.parse_args()
    main(args)
