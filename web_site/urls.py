from django.urls import path
from web_site import views

urlpatterns = [
    path("", views.home, name="home"),
]
