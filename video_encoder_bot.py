import os
import time
import telebot
import ffmpeg

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])

# Start message
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome to the video encoder bot! I can encode videos in different formats and resolutions. To get started, send me a video file.')

# Add thumbnail
@bot.message_handler(content_types=['photo'])
def add_thumbnail(message):
    global thumbnail
    global user_id
    user_id = message.chat.id
    thumbnail = message.photo[-1].file_id

# Encode video
@bot.message_handler(content_types=['video'])
def encode_video(message):
    global thumbnail
    global user_id

    # Get the video file
    video_file = message.video.file_id

    # Get the output file name
    output_file_name = user_id + '.mp4'

    # Get the video codec
    codec = 'h264'

    # Get the resolution
    resolution = '480p'

    # Start the encoding process
    start_time = time.time()
    ffmpeg.input(video_file).output(output_file_name, codec=codec, preset='veryfast', resolution=resolution).run()
    encoding_time = time.time() - start_time

    # Send the encoded video
    bot.send_message(message.chat.id, 'The video has been encoded and sent. Encoding time: {} seconds'.format(encoding_time))

    # Set the thumbnail for the user
    set_thumbnail_for_user(user_id, thumbnail)

# Get help
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Here are the available commands:
    /start - Start the bot
    /thumbnail - Add a thumbnail to the next video
    /encode - Encode a video
    /help - Get help')

# Restart the bot
@bot.message_handler(commands=['restart'])
def restart(message):
    if message.from_user.id == int(os.environ['ADMIN_ID']):
        bot.stop_bot()
        time.sleep(1)
        bot.start_bot()
        bot.send_message(message.chat.id, 'The bot has been restarted')
    else:
        bot.send_message(message.chat.id, 'You are not authorized to use this command')

# Cancel the encoding process
@bot.message_handler(commands=['cancel'])
def cancel(message):
    global thumbnail
    global user_id

    # Check if the user is allowed to cancel the process
    if message.from_user.id == int(os.environ['ADMIN_ID']) or message.chat.id == user_id:
        # Remove the thumbnail
        thumbnail = None

        # Cancel the process
        os.system('pkill -f ffmpeg')
        bot.send_message(message.chat.id, 'The encoding process has been canceled')
    else:
        bot.send_message(message.chat.id, 'You are not authorized to use this command')

# Get the download and upload speed
@bot.message_handler(commands=['speed'])
def speed(message):
    # Get the download speed
    speed = os.popen('speedtest-cli --simple').read()

    # Get the upload speed
    speed = speed.splitlines()[-1]

    # Send the speed
    bot.send_message(message.chat.id, 'Download speed: {} Upload speed: {}'.format(speed.split(' ')[0], speed.split(' ')[1]))

# Set the default resolution
def set_default_resolution(resolution):
    global default_resolution
    default
