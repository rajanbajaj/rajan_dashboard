from django.urls import path

from .controller import index

urlpatterns = [
    path("", index, name="index"),
]