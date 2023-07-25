
# MU Result Updates Telegram Bot

This Telegram bot scrapes the Mumbai University (MU) exam results website to check for new result announcements of the current year only and sends them to the specified Telegram channel. It also provides an option to run the bot locally or deploy it on Render.

> Note:
> - Local deployment - main branch
> - Render deployment - render branch

## Prerequisites

- Telegram bot token
- Telegram channel ID
- Render account
- Elephantsql account

## Environment Variables

To run this project, you will need to add the following environment variables while creating new web service

### Get a Telegram Bot token

&nbsp; 1. Visit <https://t.me/BotFather> or find `@BotFather` on your Telegram to register a new bot. 

&nbsp; 2. Send `/newbot` command to BotFather.

&nbsp; 3. Set a name for the bot and a username (ending with 'bot').

&nbsp; 4. When registration process is completed, BotFather will provide an HTTP API token for the bot.

### Get the channel ID

&nbsp; 1. Create a new channel and post any message in it.

&nbsp; 2. Forward that message to <https://t.me/get_id_channel_bot>.

&nbsp; 3. The bot will give the unique ID of your channel.

### Get the database url from [Elephantsql](https://www.elephantsql.com/)

&nbsp; 1. Create a new account.

&nbsp; 2. Create a new instance by giving a name, keep plan and region as default.

&nbsp; 3. Go to the instance you created just now and copy the url.

### Database setup
&nbsp; 1. Head to the browser tab in your instance and run the following query:
```sql
CREATE TABLE result_count (
    count INTEGER
);

INSERT INTO result_count (count) VALUES (0);
```
&nbsp; This will add a column count with value 0 to the table result_count. You can insert other count value to get results after a specific count.

&nbsp; 2. To update the value anytime. Run the following query:
```sql
UPDATE result_count SET count = 100;
```
&nbsp; This will update the count to 100. Replace 100 with the count you want.

### Bot setup

&nbsp; 1. Add the bot to your channel.

&nbsp; 2. Give admin rights to the bot.

## Render Deployment

The bot can be deployed freely on <https://render.com> as a web application.

## Set up Render

&nbsp; 1. Make sure you have a Github repo containing all the files.

&nbsp; 2. Get yourself a render.com account (Logging in with your github account should be the most convenient).

&nbsp; 3. Follow these clicks: Dashboard >> New >> Web Service.

&nbsp; 4. Choose your Github repo or you can paste your public github repo link.

&nbsp; 5. Complete the form with:

- Name: Any
- Region: Any
- Branch: render
- Runtime: Docker
- Instance Type: Free
- Click on Advanced and add the 3 keys as environment variables(`BOT_TOKEN`, `CHANNEL_ID`, & `DATABASE_URL`)
- Auto-Deploy: No

## Deploy

&nbsp; 1. For the first time, click Create Web Service after filling out the form to start deploying the bot.

&nbsp; 2. Manual deployment can be performed in your bot web service found in Dashboard of render.

> Note:
> - It is important to select `render` branch else the deployment will fail.
> - The 3 keys (`BOT_TOKEN`, `CHANNEL_ID`, & `DATABASE_URL`) and their values don't need quotes.
> - Logs can be found on <https://{your_setup_name}.onrender.com/log> and additional bash command can be executed on <https://{your_setup_name}.onrender.com/terminal>
> - Deployment will take about 15 minutes to complete. (Usually, the bot will get duplicated responses for a while. Wait it out. It will stop eventually.)

## Possible Improvements

- Add more functionalities to the bot.
- Track previous year and revaluation results.
- Track edited results.

## Telegram Channel: `@mu_result_updates`

Join the Telegram channel [here](https://t.me/mu_result_updates) to receive the latest current year MU exam results as soon as they are announced.

Please note that the bot's availability depends on the Mumbai University exam results website and the Telegram API. In case of any issues, you can check the logs or contact [me](https://t.me/shubham_indalkar) for assistance.

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the GitHub repository.

**Happy result updates!**

## Contributing

We are grateful for contributions of any magnitude.

