
# MU Result Updates Telegram Bot

This Telegram bot scrapes the Mumbai University (MU) exam results website to check for new result announcements of the current year only and sends them to the specified Telegram channel. It also provides an option to run the bot locally or deploy it on Render.

> Note:
> - Local deployment - main branch
> - Render deployment - render branch

## Prerequisites

- Git 
- Python 3.10 or higher 
- Telegram bot token
- Telegram channel ID

## Installation

&nbsp; 1. Clone the repository
```bash
  git clone https://github.com/shubham-indalkar/mu-results-update-tg-bot.git
```
&nbsp; 2. Change directory
```bash
  cd mu-results-update-tg-bot
```
&nbsp; 3. Install python dependencies
```bash
  pip3 install -r requirements.txt
```
&nbsp; or
```bash
  pip install -r requirements.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

### Get a Telegram Bot token

&nbsp; 1. Visit <https://t.me/BotFather> or find `@BotFather` on your Telegram to register a new bot.

&nbsp; 2. Send `/newbot` command to BotFather.

&nbsp; 3. Set a name for the bot and a username (ending with 'bot').

&nbsp; 4. When registration process is completed, BotFather will provide an HTTP API token for the bot.

### Get the channel ID

&nbsp; 1. Create a new channel and post any message in it.

&nbsp; 2. Forward that message to <https://t.me/get_id_channel_bot>.

&nbsp; 3. The bot will give the unique ID of your channel.

### Bot setup

&nbsp; 1. Add the bot to your channel.

&nbsp; 2. Give admin rights to the bot.


### Declare your keys in environment

Running the bot in local will required creating an `.env` file with the following contents:

```python
BOT_TOKEN="YOUR_BOT_TOKEN"
CHANNEL_ID=YOUR_CHANNEL_ID
```

> Note:
> - `BOT_TOKEN` should be put as String and `CHANNEL_ID` should be put as Integer.
> - For security, `.env` file is only suitable for local run. In case of deployment, your keys should be kept as `SECRETS` or `ENVIRONMENT VARIABLES` that can only be accessed by you (checkout render branch).

## Local Deployment

&nbsp; 1. Set the *count* variable of `count.json` to 0 if you want to fetch all the result of current year or set to specific value to get results after certain count.

&nbsp; 2. Run the script
```bash
  python3 channel.py
```
&nbsp; or
```bash
  python channel.py
```

## Possible Improvements

- Add more functionalities to the bot.
- Track previous year and revaluation results.
- Track edited results.

## Telegram Channel: `@mu_result_updates`

Join the Telegram channel [here](https://t.me/mu_result_updates) to receive the latest current year MU exam results as soon as they are announced.

Please note that the bot's availability depends on the Mumbai University exam results website and the Telegram API. In case of any issues, you can check the logs or contact [me](https://t.me/shubham_indalkar) for assistance.

**Note:** Make sure to keep the `count.json` file in the same directory as the bot script. It stores the count of declared results and ensures that only new results are posted.

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the GitHub repository.

**Happy result updates!**

## Contributing

We are grateful for contributions of any magnitude.

