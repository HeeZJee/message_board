from django import urls
from django.urls import path
from posts.views import  HomPageView

urlpatterns = [
    path('', HomPageView.as_view(),name='home' )
    ]