from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("hossein", views.hossein, name="hossein"),
    path("narges", views.narges, name="narges"),
    path("<str:name>", views.greeting, name="greeting")
]