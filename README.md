# YouTube-api

## Pre-requisites

1. ```Python version>=3.8```
2. ```RabbitMQ server``` For asynchronous calls to Youtube API
3. Google API Key(To be inserted [this](YoutubeFam/YoutubeApi/tasks.py) file)

Inorder to install RabbitMQ server in UBUNTU --

```sudo apt-get install rabbitmq-server```

Then, start the server by

```
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```

Now, following step are to be performed on command line after cloning this repo and coming to this readme’s directory—

1.	```pip install pipenv```  To create the virtual Environment

2.	```pipenv shell```   This will activate a virtual environment and install required dependencies.

3.	```cd YoutubeFam```

4.	```python manage.py runserver``` TO start the main server

5. In a seprate terminal with same root directory, run below commands

```pip install pipenv```

```celery -A cryptocurrencytracking worker -l info``` To start celery process(For continous call to API database will be updated every 15 seconds)

Now both APIs(for getting latest video information and search API) are paginated and have a browsable interface.

Information returned by API includes

1. Thumbnail URL
2. Video Title
3. Video description
4. Published Time
5. Video ID

To use Video info. API(According to descending order of time)--

```http://127.0.0.1:8000/apitube/```

Search API can be consumed as followed--

http://127.0.0.1:8000/find/<one_word_search>/

example - http://127.0.0.1:8000/find/cricket/

