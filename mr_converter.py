import sys
from pytube import YouTube

from moviepy.editor import *


video_link = sys.argv[1]
try:
    print('Start downloading and converting {} to mp3'.format(video_link))
    video_path = YouTube(video_link).streams.first().download('/home/antunesleo/projects/youtube-to-mp3/videos')
    print('Video download complete, starting convertion!')
    audio_name = video_path.split('/')[-1:][0].split('.')[0]
    audio_path = '/home/antunesleo/Music/Downloaded/{}.mp3'.format(audio_name)
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    print('YEEEEES, LETS LISTEN TO SOME GOOD MUSIC, BIIITCH!')
except Exception as ex:
    print('DAMMIT! Something went wrong {}'.format(str(ex)))
