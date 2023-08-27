import os
import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Bot token
TOKEN = os.getenv("BOT_TOKEN")

# Owner name
OWNER = "bankai"

# Default thumbnail
THUMBNAIL = "thumbnail.jpg"

# Custom message
CUSTOM_MESSAGE = ""

# Default resolution
RESOLUTION = "480p"

# Default video codec
VIDEO_CODEC = "h264"

# Admins
ADMINS = ["1234567890"]

# Watermark
WATERMARK = "@aniimax"

# Updater
updater = Updater(TOKEN, use_context=True)

# Handlers
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
resolution_handler = CommandHandler("resolution", resolution)
speed_handler = CommandHandler("speed", speed)
thumbnail_handler = MessageHandler(Filters.photo, thumbnail)
video_codec_handler = CommandHandler("video_codec", video_codec)
restart_handler = CommandHandler("restart", restart)
cancel_handler = CommandHandler("cancel", cancel)

# Add handlers to dispatcher
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(resolution_handler)
updater.dispatcher.add_handler(speed_handler)
updater.dispatcher.add_handler(thumbnail_handler)
updater.dispatcher.add_handler(video_codec_handler)
updater.dispatcher.add_handler(restart_handler)
updater.dispatcher.add_handler(cancel_handler)

# Start the bot
updater.start_polling()

# Keep the bot running
updater.idle()

def start(update, context):
    # Send a welcome message
    update.message.reply_text(
        f"Welcome to the video encoder bot! I can encode videos using ffmpeg.\n\n"
        f"My owner is {OWNER}.\n\n"
        f"The default resolution is {RESOLUTION}.\n\n"
        f"The default video codec is {VIDEO_CODEC}.\n\n"
        f"To get started, use the /help command."
    )

def help(update, context):
    # Send a help message
    update.message.reply_text(
        f"Here are the available commands:\n\n"
        f"/start - Get started\n"
        f"/help - Show this help message\n"
        f"/resolution - Change the video encoding resolution\n"
        f"/speed - Show the download and upload speed\n"
        f"/thumbnail - Set the thumbnail for the next video\n"
        f"/video_codec - Change the video encoding codec\n"
        f"/restart - Restart the bot\n"
        f"/cancel - Cancel the currently encoding file process\n"
        f"/watermark - Add a watermark to the encoded video"
    )

def resolution(update, context):
    # Get the new resolution from the user
    resolution = update.message.text

    # Set the new resolution
    global RESOLUTION
    RESOLUTION = resolution

    update.message.reply_text(f"Resolution set to {RESOLUTION}.")

def speed(update, context):

