import argparse
import random
import tomllib
from argparse import Namespace


def main(args: Namespace) -> None:
    with open(args.config, "rb") as f:
        data = tomllib.load(f)

    chance = data["billy1buttsbot"]["chance_of_buttification"]
    print(f"Chance of buttification: {chance}")

    roll = random.random()

    if roll < chance:
        print("Buttify!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Billy1ButtsBot service')
    parser.add_argument('--config', default='pyproject.toml', help='Configuration')
    parser.add_argument('--user', default='billy1buttsbot', help='User')
    parser.add_argument('--password', help='Password', required=True)

    args = parser.parse_args()
    main(args)
