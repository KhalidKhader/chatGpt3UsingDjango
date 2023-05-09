from django.urls import path     
from .import views
urlpatterns = [
    path('', views.index),	
    path('chatGpt', views.chatGpt),
    path('openAiChatGpt',views.openAiChatGpt),   
    path('transaltor', views.transaltor),
    path('openAiTransaltor',views.openAiTransaltor), 
    path('jsToPython', views.jsToPython),
    path('openAiJsToPython',views.openAiJsToPython), 
]
