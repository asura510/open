from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'webui/index.html')
def brave(request):
    return render (request, 'webui/brave-rewards-verification.txt')
