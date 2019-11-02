import os
import requests
import json
import time
from urllib.parse import urlencode
from download_video import download_video_as_mp3

API_KEY = 'AIzaSyBPMZNeesYEU7bRatKXtxUlDOEKzULN78E'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3'
MAX_TIMEOUT = 60 # give up if we don't get response after a minute
ACCESS_TOKEN = ''

BASE_VIDEO_URL = 'youtube.com/watch?v='


def call_endpoint(endpoint, params_dict={}):
    url_encoded_params = f'?key={API_KEY}'
    if len(params_dict):
        url_encoded_params += '&'
        url_encoded_params += urlencode(params_dict)
    full_url = f'{YOUTUBE_API_URL}/{endpoint}{url_encoded_params}'
    response = requests.get(full_url, MAX_TIMEOUT)
    return response.text

def call_endpoint_authorized(endpoint, params_dict={}):
    params_dict["access_token"] = ACCESS_TOKEN
    return call_endpoint(endpoint, params_dict)


# authorization_params = {}
# auth_response = call_endpoint('AUTHORIZE', authorization_params)
# print(auth_response)


# channel_dict = {
#     "part": 'snippet',
#     "forUsername": 'yhigma',
# }
# channels_resp = call_endpoint('channels', channel_dict)
# print(channels_resp)
YOUTUBE_CHANNEL_ID = 'UC0E_mgLaw-Of81rmGp35DsA'


# playlists_params = {
#     "mine": True,
#     "part": 'snippet',
# }
# playlists_params = {
#     "channelId": YOUTUBE_CHANNEL_ID,
#     "part": 'snippet',
# }
# playlists_resp = call_endpoint('playlists', playlists_params)
# print(playlists_resp)
FUNKALICIOUS_ID = 'PLPe4EdBAhKC4UwLHudo0f0dsid-nJZR3S'

playlist_items_dict = {
    "part": 'contentDetails',
    # "playlistId": WATCH_LATER_PLAYLIST_ID,
    "playlistId": FUNKALICIOUS_ID,
}
playlist_videos_resp = call_endpoint('playlistItems', playlist_items_dict)
print(playlist_videos_resp)

video_ids = []
playlist_vids_dict = json.loads(playlist_videos_resp)
for video_dict in playlist_vids_dict["items"]:
    video_id = video_dict["contentDetails"]["videoId"]
    video_ids.append(video_id)


MP3_VIDEO_ENDPOINT_1 = 'https://ytmp3.cc/'
print('download these videos:')
for video_id in video_ids:
    video_url = 'https://' + BASE_VIDEO_URL + video_id
    download_video_as_mp3(video_url)


