from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('.well-known/brave-rewards-verification.txt/', views.brave, name='brave'),
]
