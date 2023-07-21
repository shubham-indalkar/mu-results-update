# Use the official Python image as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the files from your GitHub repo to the container's working directory
COPY . /app

# Install the required dependencies
RUN pip install -r requirements.txt

# Run your Telegram bot script
CMD ["python", "channel_bot.py"]
