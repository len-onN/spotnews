from django.shortcuts import render
from news.models import News


# Create your views here.
def index(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)
