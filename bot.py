import os
import re

import ffmpeg
import telegram

def encode_video(video_file, output_file, watermark):
    """Encodes a video file using ffmpeg and adds a watermark.

    Args:
        video_file (str): The path to the video file.
        output_file (str): The path to the output file.
        watermark (str): The path to the watermark image.
    """
    ffmpeg.input(video_file).output(output_file).overwrite_output().video_filter("scale", width=480, height=360).video_filter("drawtext", text=watermark, x=10, y=10, fontcolor="white", fontsize=20).run()

def get_file_name(video_file):
    """Gets the file name of the video file without the extension and then adds a timestamp to the file name.

    Args:
        video_file (str): The path to the video file.

    Returns:
        str: The file name of the video file without the extension.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{timestamp}_{get_file_name(video_file)}"

def get_watermark_text(chat_id):
    """Gets the watermark text for the given chat ID.

    Args:
        chat_id (str): The chat ID.

    Returns:
        str: The watermark text.
    """
    if chat_id == "YOUR_CHAT_ID":
        return "@aniimax"
    else:
        return "Chat watermark"

def main():
    """The main function of the app."""
    bot = telegram.Bot(token="YOUR_BOT_TOKEN")

    @bot.message_handler(commands=["encode"])
    def encode_video(message):
        """Encodes a video file and sends the output file to the user.

        Args:
            message (telegram.Message): The message from the user.
        """
        video_file = message.text.split(" ")[1]
        output_file = f"{get_file_name(video_file)}_encoded.mp4"
        watermark = get_watermark_text(message.chat_id)

        encode_video(video_file, output_file, watermark)

        bot.send_message(message.chat_id, f"The encoded video has been saved to {output_file}.\n\nVideo provided by @aniimax")

bot.polling()

if __name__ == "__main__":
    main()
  
