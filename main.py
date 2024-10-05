import argparse
import random
import tomllib
from argparse import Namespace


def main(args: Namespace) -> None:
    with open(args.config, "rb") as f:
        data = tomllib.load(f)

    print(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Billy1ButtsBot service')
    parser.add_argument('--config', default='pyproject.toml', help='Configuration')
    parser.add_argument('--user', default='billy1buttsbot', help='User')
    parser.add_argument('--password', help='Password', required=True)

    args = parser.parse_args()
    main(args)
