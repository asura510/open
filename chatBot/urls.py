from django.urls import path
from . import views
urlpatterns = [
path('chatbot/<str:command>', views.bot, name='bot'),
]
