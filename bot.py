import os
import time
import pyrogram 
from pyrogram import Client

client = Client("my_bot", api_id=20210345, api_hash="11bcb58ae8cfb85168fc1f2f8f4c04c2")

@client.register_handler(filters.command("start"))
def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Welcome to my bot!")

client.run() ,
filters

# Initialize the bot
bot = Client("my_bot", api_id=20210345, api_hash="11bcb58ae8cfb85168fc1f2f8f4c04c2")

# Get the authorized users
authorized_users = ["@aniimax"]

# Get the start message
start_message = """
This is a Telegram bot that can encode video to 480p using FFmpeg. It can also add "provided by @aniimax" and a watermark "@aniimax" at the top right corner.

To use the bot, send a video file to it. The bot will start encoding the video immediately. You can track the progress of the encoding in the chat.

The start message can be edited by authorized users only.
"""

# Get the thumbnail
thumbnail = "https://example.com/thumbnail.jpg"

# Get the restart option
restart_option = "restart"

# Get the custom message
custom_message = "(Edited by admin)"

# The main function
def main():

    # Register a handler for the "/help" command
    bot.on(filters.command("help"), help)

    # Register a handler for the "/resolution" command
    bot.on(filters.command("resolution"), resolution)

    # Register a handler for the "/speed" command
    bot.on(filters.command("speed"), speed)

    # Register a handler for the "/restart" command
    bot.on(filters.command("restart"), restart)

    # Start the bot
    bot.run()

# The "/start" command handler
def start(update, context):
    # Check if the user is authorized
    if update.effective_user not in authorized_users:
        return

    # Send the start message
    context.bot.send_message(update.effective_chat.id, start_message)

# The "/help" command handler
def help(update, context):
    # Send a message with all the available commands
    context.bot.send_message(update.effective_chat.id, """
Available commands:

/start - Show the start message
/help - Show this help message
/resolution - Change the video encoding resolution
/speed - Show the download and upload speed
/restart - Restart the bot
""")

# The "/resolution" command handler
def resolution(update, context):
    # Check if the user is authorized
    if update.effective_user not in authorized_users:
        return

    # Get the new resolution
    new_resolution = update.message.text

    # Update the global variable
    global resolution
    resolution = new_resolution

    # Send a message confirming the new resolution
    context.bot.send_message(update.effective_chat.id, f"The new resolution is {resolution}.")

# The "/speed" command handler
def speed(update, context):
    # Get the download speed
    download_speed = context.bot.get_download_speed()

    # Get the upload speed
    upload_speed = context.bot.get_upload_speed()

    # Send a message with the download and upload speeds
    context.bot.send_message(update.effective_chat.id, f"Download speed: {download_speed} Upload speed: {upload_speed}")

# The "/restart" command handler
def restart(update, context):
    # Check if the user is authorized
    if update.effective_user not in authorized_users:
        return

    # Restart the bot
    bot.restart()

# Run the main function
if __name__ == "__main__":
    main()
    
