from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .serializers import YTSerializer

from rest_framework.pagination import PageNumberPagination

from .models import YoutubeData

from rest_framework.decorators import api_view

from rest_framework.response import Response


@api_view(['GET'])
def api_search(request,q):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    title_search = YoutubeData.objects.filter(title__contains=q)
    description_search = YoutubeData.objects.filter(description__contains=q)
    search_result = (title_search | description_search).distinct().order_by('-publish_time')
    result_page = paginator.paginate_queryset(search_result, request)
    serializer = YTSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def api_vids(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    q = YoutubeData.objects.all().order_by('-publish_time')
    result_page = paginator.paginate_queryset(q, request)
    serializer = YTSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
