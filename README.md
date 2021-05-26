# YouTube-api

## Running using Docker

1. Clone this repositoy to your system
2. Add the developer_key for youtube API in [this](YoutubeFam/YoutubeApi/tasks.py) file. 
3. Run ```docker-compose up``` command.

Now both APIs(for getting latest video information and search API) are paginated and have a browsable interface.

Information returned by API includes

1. Thumbnail URL
2. Video Title
3. Video description
4. Published Time
5. Video ID

To use Video information API(According to descending order of time)--

```http://127.0.0.1:8000/apitube/```

Search API can be consumed as followed--

```http://127.0.0.1:8000/find/<one_word_search>/```

example - ````http://127.0.0.1:8000/find/cricket/```

