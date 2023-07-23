# Use a specific Python version as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the files from your current directory to the container's working directory
COPY . /app

# Install the required dependencies
RUN pip install -U pip && pip install -U -r requirements.txt

# Run your Telegram bot script
CMD ["python", "channel_bot.py"]

