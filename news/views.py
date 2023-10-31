from django.shortcuts import render, get_object_or_404
from news.models import News


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {"news": get_object_or_404(News, id=id)}
    return render(request, 'news_details.html', context)
