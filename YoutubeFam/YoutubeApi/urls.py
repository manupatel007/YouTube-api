from django.urls import path
from . import views

urlpatterns = [
    path("find/<str:q>/", views.api_search, name="apisearch"),
    path("apitube/", views.api_vids, name="apivids")
]