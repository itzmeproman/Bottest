import os
import time
import telebot
import ffmpeg

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])

# Start message
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome to the video encoder bot! I can encode videos in different formats and resolutions. To get started, send me a video file in MKV or MP4 format.')

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
    resolution = get_default_resolution()

    # Check the file extension
    file_extension = os.path.splitext(video_file)[1]
    if file_extension not in ['.mkv', '.mp4']:
        bot.send_message(message.chat.id, 'Sorry, I can only encode videos in MKV or MP4 format.')
        return

    # Start the encoding process
    start_time = time.time()
    ffmpeg.input(video_file).output(output_file_name, codec=codec, preset='veryfast', resolution=resolution).run()

    # Send the progress to the user
    progress = 0
    while progress < 100:
        progress = int(ffmpeg.progress())
        bot.send_message(message.chat.id, 'Download progress: {}%'.format(progress))
        time.sleep(1)

    encoding_time = time.time() - start_time

    # Send the encoded video
    bot.send_message(message.chat.id, 'The video has been encoded and sent. Encoding time: {} seconds'.format(encoding_time))

    # Set the thumbnail for the user
    set_thumbnail_for_user(user_id, thumbnail)

