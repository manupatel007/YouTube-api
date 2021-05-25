from time import sleep
from celery import shared_task

from .models import YoutubeData
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


DEVELOPER_KEY = 'AIzaSyAJkIHsN0svj3vchfggaonFTsj4oNo2gnA'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


@shared_task
def youtube_search(initial_date):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
    q="corona",
    part='id,snippet',
    maxResults=10,
    publishedAfter=initial_date,
    ).execute()

    

    mx_date = initial_date
    for search_result in search_response.get('items', []):
        #print(search_result)
        mx_date = max(mx_date, search_result['snippet']['publishedAt'])
        #print(search_result['snippet']['thumbnails']['medium']['url'])
        a = YoutubeData(thumbnail=search_result['snippet']['thumbnails']['medium']['url'],
        title=search_result['snippet']['title'] , 
        description=search_result['snippet']['description'], 
        publish_time= search_result['snippet']['publishedAt'], 
        video_id=search_result['id']['videoId']
        )
        a.save()
    return mx_date

initial_date = "2020-11-05T07:20:39Z"
while(1):
    sleep(15)
    print("a",initial_date)
    initial_date = youtube_search(initial_date)