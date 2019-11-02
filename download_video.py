""" Wrapper downloading a YouTube video youtube_dl's api """
from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'download_archive': 'archive.txt',
    'format': 'bestaudio/best',
    'outtmpl': 'media/%(title)s-%(id)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # 'logger': MyLogger(),
    # 'progress_hooks': [my_hook],
}

def download_video_as_mp3(video_url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

