**Stupidly simple way to send your pc screenshots by Telegram bot.**


## Prerequirements

- Python 3.8+

## How to setup

- Clone the repository
- Copy `.env.example` to `.env`
- Open [my.telegram.org](my.telegram.org) create new application
- Copy `api_id` and `api_hash` to `.env`
- Create a bot in @BotFather
- Copy bot token to `.env`
- Install requirements with `pip install -r requirements.txt`
- Run `python3 remscreen.py`

## How to use

For get screenshots send `/screen {hostname}` to bot, where `{hostname}` is your pc hostname. For example `/screen ISAAC-PC`.

On Windows hostname is computer name, for Linux hostname is `hostname -f`.