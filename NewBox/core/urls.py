from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/downloaded', views.download, name="download"),
]
