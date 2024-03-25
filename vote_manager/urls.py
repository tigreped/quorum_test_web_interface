from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("votes/", views.votes, name="votes"),
    path("load_data/", views.load_data, name="load_data")
]
