from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.forms import CreateNewsForm


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {"news": get_object_or_404(News, id=id)}
    return render(request, 'news_details.html', context)


def news_forms(request):
    forms = CreateNewsForm()
    if request.method == "POST":
        forms = CreateNewsForm(request.POST)
        if forms.is_valid():
            Category.objects.create(**forms.cleaned_data)
            return redirect("home-page")
    context = {"forms": forms}
    return render(request, 'categories_form.html', context)
