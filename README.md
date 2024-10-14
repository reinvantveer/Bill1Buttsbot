# Billy1Buttsbot
Twitch bot for Billy1Kirby

## Installation

1. Clone or download contents of the repository. Downloading requires you to extract the contents of the zip file every
   time you want to update the bot, so cloning is recommended
2. Run `poetry install` to install dependencies
3. Edit the top contents of pyproject.toml to adjust the settings to your liking, but it should work out of the box
4. Run `poetry run python -m main` to start the bot. It will ask you for your Twitch username and OAuth token, which you
   can get from [here](https://twitchapps.com/tmi/), choose "Connect", authorize access and copy the OAuth token.
5. Enjoy!
6. If you want to run the bot in the background, you can use `poetry run python -m main &` on Linux or `start poetry run python -m main` on Windows
7. If you want to stop the bot, you can use `pkill -f "python -m main"` on Linux or `taskkill /f /im "python.exe" /fi "WINDOWTITLE eq poetry run python -m main"` on Windows
8. If you want to update the bot, you can use `git pull` to get the latest changes, and then run `poetry install` to update the dependencies

## Features
- [x] Buttification of random messages
- 