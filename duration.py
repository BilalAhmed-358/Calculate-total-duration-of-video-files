import os
import mimetypes
from moviepy.editor import VideoFileClip
import sys
import tkinter as tk

def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_video_length(file_path):
    video = VideoFileClip(file_path)
    duration = video.duration
    video.close()
    return duration

def outputOnScreen(sentence,textComponent):
    textComponent.insert(tk.END, sentence)
    textComponent.update()


def calculate_total_video_length(directory,textComponent):
    total_length = 0
    count=0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is a video
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type and mime_type.startswith('video'):
                # Get the video length and add it to total_length
                video_length = get_video_length(file_path)
                # print("Video: ", file)
                timeLength=convert_seconds_to_hms(round(video_length))
                # print(convert_seconds_to_hms(round(video_length)), "\n")
                total_length += video_length
                sentence = "Video: " + file + "\n" + timeLength + "\n"
                outputOnScreen(sentence,textComponent)


    outputString= "The total duration of videos in the folder is "+ convert_seconds_to_hms(round(total_length))+"\n"
    textComponent.insert(tk.END, outputString)
