from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import argparse
from .models import YoutubeData
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'My_Key'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

#def youtube_search(options):
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
developerKey=DEVELOPER_KEY)

# Call the search.list method to retrieve results matching the specified
# query term.
search_response = youtube.search().list(
q="cricket",
part='id,snippet',
maxResults=10
).execute()

videos = []
channels = []
playlists = []

# Add each result to the appropriate list, and then display the lists of
# matching videos, channels, and playlists.
for search_result in search_response.get('items', []):
    print(search_result)
    print(search_result['snippet']['thumbnails']['medium']['url'])
    a = YoutubeData(thumbnail=search_result['snippet']['thumbnails']['medium']['url'], title=search_result['snippet']['title'] , description=search_result['snippet']['description'], publish_time= search_result['snippet']['publishedAt'])
    a.save()
    if search_result['id']['kind'] == 'youtube#video':
        videos.append('%s (%s) %s' % (search_result['snippet']['title'], search_result['snippet']['description'],
                                    search_result['id']['videoId']))
    elif search_result['id']['kind'] == 'youtube#channel':
        channels.append('%s (%s) %s' % (search_result['snippet']['title'], search_result['snippet']['description'],
                                    search_result['id']['channelId']))
    elif search_result['id']['kind'] == 'youtube#playlist':
        playlists.append('%s (%s) %s' % (search_result['snippet']['title'], search_result['snippet']['description'],
                                    search_result['id']['playlistId']))

    print('Videos:\n', '\n'.join(videos), '\n')
    print('Channels:\n', '\n'.join(channels), '\n')
    print('Playlists:\n', '\n'.join(playlists), '\n')

def home(request):
    return HttpResponse("Hiii!!!")