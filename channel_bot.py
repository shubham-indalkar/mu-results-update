import time
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import logging
from telegram import Bot
from webserver import keep_alive

# Set up logging for debugging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token and channel ID
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Create a single Bot instance to be reused
bot = Bot(token=TOKEN)

# Function to post list of messages on the Telegram channel
async def post_messages(messages):
    try:
        for message in messages:
            await bot.send_message(CHANNEL_ID, text=message)
            logger.info("Message sent to the Telegram channel successfully.")
            time.sleep(35)  # Add a small delay between sending messages to avoid rate-limiting
    except Exception as e:
        logger.error(f"Failed to send message: {e}")

async def main():
    url = "http://www.mumresults.in/"
    while True:
        try:
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")

            # Find the table with class name "countertwo"
            table = soup.find("table", class_="countertwo")

            if table:
                # Find all the rows (tr tags) within the table
                rows = table.find_all("tr")

                # Load the previous count of declared results from the file
                try:
                    with open("count.json", "r") as file:
                        previous_count = json.load(file)["count"]
                except (FileNotFoundError, json.JSONDecodeError):
                    previous_count = 0

                # Get the current count of declared results
                current_count = len(rows)

                # If there are new results, post them on the Telegram channel
                if current_count > previous_count:
                    new_results = rows[previous_count:]
                    messages = []
                    for row in new_results:
                        # Find all the td tags within the current tr tag
                        td_tags = row.find_all("td")

                        # Check if there are at least 4 td tags in the row (to avoid IndexErrors)
                        if len(td_tags) >= 4:
                            # Extract the program code (2nd td tag)
                            program_code = td_tags[1].get_text(strip=True)

                            # Extract the result date (4th td tag)
                            result_date = td_tags[3].get_text(strip=True)

                            # Find the exam information (3rd td tag)
                            exam_info = td_tags[2]

                            # If the exam_info contains a 'span' tag, use that; otherwise, use the 'a' tag directly
                            span_tag = exam_info.find("span")
                            a_tags = span_tag.find_all("a") if span_tag else exam_info.find_all("a")

                            # Construct the message with the result information
                            message = f"{result_date}\n{program_code}\n\n"
                            for a_tag in a_tags:
                                a_text = a_tag.get_text(strip=True)
                                href_link = a_tag.get("href")
                                message += f"{a_text}\n{url}{href_link}\n\n"
                            messages.append(message)

                    # Post the messages on the Telegram channel (await it since it's an asynchronous function)
                    await post_messages(messages)

                    # Update the count file with the current count
                    with open("count.json", "w") as file:
                        json.dump({"count": current_count}, file)

            else:
                # print("No new results.")
                pass

        except Exception as e:
            logger.error(f"Failed to fetch website data: {e}")
            time.sleep(60)  # Wait for 1 minute before retrying

        # delay between checking for new results
        time.sleep(30)

if __name__ == "__main__":
    # Call the keep_alive function to start the web server
    keep_alive()
    
    import asyncio
    asyncio.run(main())
