# Billy1Buttsbot

Have you ever felt like your Twitch chat was missing something? Butts, specifically? Well, now you can add a bot that
will buttify your chat! This is a simple Twitch bot for Billy1Kirby but you can use it for your own channel as well. It
will buttify random messages in chat, and you can configure the chance of a message being buttified.

## Installation
1. Clone or download contents of the repository. Downloading requires you to extract the contents of the zip file every
   time you want to update the bot, so cloning is recommended
2. Install python 3.11 or later from [here](https://www.python.org/downloads/)
3. Open a command prompt or terminal in the directory where you downloaded the bot code
4. Run `python -m pip install poetry` to install poetry
5. Run `poetry install` to install dependencies
6. Edit the top contents of pyproject.toml to adjust the [tool.billy1buttsbot] section to your liking, but it should work out of the box

## Usage

1. Run `poetry run python -m main --token=oauth:abcdefghijklmnop --verbose` to start the bot. Especially in the
   beginning, it helps to run the bot in debug level logging, using `--verbose`. It will ask you for your Twitch
   username and OAuth token, which you can get from [here](https://twitchapps.com/tmi/), choose "Connect", authorize
   access and copy the OAuth token.
3. If you want to run the bot in the background, you can use `poetry run python -m main &` on Linux or `start poetry run python -m main` on Windows
4. If you want to stop the bot, you can use `pkill -f "python -m main"` on Linux or `taskkill /f /im "python.exe" /fi "WINDOWTITLE eq poetry run python -m main"` on Windows
5. If you want to update the bot, you can use `git pull` to get the latest changes, and then run `poetry install` to update the dependencies

## Features
- [x] Buttification of random messages
- 