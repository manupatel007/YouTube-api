from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("videos/", views.videos, name="videos"),
    path("youtube/", views.paginated_vids, name="paginated"),
    path("search/<q>/", views.search_vids, name="search"),
]