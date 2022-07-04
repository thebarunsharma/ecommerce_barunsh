from django.urls import path
from .views import index,about,destination,blog,singleblog
urlpatterns = [
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('travel_destination.html', destination),
    path('blog.html',blog),
    path('single-blog.html',singleblog)
]