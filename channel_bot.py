import time
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import logging
import psycopg2
from telegram import Bot
from webserver import keep_alive

# Set up logging for debugging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token and channel ID
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
# Parse the DATABASE_URL from the environment variable
DATABASE_URL = os.environ["DATABASE_URL"]

# Create a single Bot instance to be reused
bot = Bot(token=TOKEN)

# Function to connect to the ElephantSQL database and fetch the count
def get_and_cache_count():
    conn = psycopg2.connect(DATABASE_URL)
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT count FROM result_count;")
            count = cursor.fetchone()[0]
            logger.info("Count from database: ", count)
            return count
    except psycopg2.Error as e:
        logger.error(f"Failed to fetch count from the database: {e}")
        return None
    finally:
        conn.close()

# Function to update the count variable in ElephantSQL
def update_count_in_database(count):
    conn = psycopg2.connect(DATABASE_URL)
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE result_count SET count = %s;", (count,))
        conn.commit()
    except psycopg2.Error as e:
        logger.error(f"Failed to update count in the database: {e}")
    finally:
        conn.close()

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
    # Fetch the count from ElephantSQL and cache it
    cached_count = get_and_cache_count()

    URL = "http://www.mumresults.in/"
    while True:
        try:
            page = urlopen(URL)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")

            # Find the table with class name "countertwo"
            table = soup.find("table", class_="countertwo")

            if table:
                # Find all the rows (tr tags) within the table
                rows = table.find_all("tr")

                # Get the current count of declared results
                current_count = len(rows)

                # If there are new results, post them on the Telegram channel
                if current_count > cached_count:
                    new_results = rows[cached_count:]
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
                                message += f"{a_text}\n{URL}{href_link}\n\n"
                            messages.append(message)

                    # Post the messages on the Telegram channel (await it since it's an asynchronous function)
                    await post_messages(messages)

                    # Update the cached count
                    cached_count = current_count
                    # Update the count variable in ElephantSQL
                    update_count_in_database(current_count)

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
