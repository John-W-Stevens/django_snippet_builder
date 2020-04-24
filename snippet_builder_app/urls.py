from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
        # GET -> display snippet builder
        # POST -> handle error message submission
    path("snippet_builder", views.snippet_builder),
]