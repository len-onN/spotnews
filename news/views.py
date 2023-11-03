from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category, User
from news.forms import CreateCategoryForm, CreateNewsForm


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    context = {"news": get_object_or_404(News, id=id)}
    return render(request, 'news_details.html', context)


def category_forms(request):
    forms = CreateCategoryForm()
    if request.method == "POST":
        forms = CreateCategoryForm(request.POST)
        if forms.is_valid():
            Category.objects.create(**forms.cleaned_data)
            return redirect("home-page")
    context = {"forms": forms}
    return render(request, 'categories_form.html', context)


def new_news_forms(request):
    form = CreateNewsForm()
    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data.pop("categories")
            data = News.objects.create(**form.cleaned_data)
            data.categories.set(category)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "news_form.html", context)

