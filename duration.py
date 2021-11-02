#Just a file to get the durations of the videos for json
import os
import json
from moviepy.video.io.VideoFileClip import VideoFileClip

f = open('main.json')
data = json.load(f)

index = 0
for i in data['overall']:
    clip = VideoFileClip(i['path' + str(index)])
print(clip.duration)