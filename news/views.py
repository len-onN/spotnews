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
    forms = CreateNewsForm()
    if request.method == "POST":
        forms = CreateNewsForm(request.POST, request.FILES)
        if forms.is_valid():
            category = forms.cleaned_data.pop("categories")
            author_id = forms.cleaned_data['author']
            author = User.objects.get(id=author_id)
            news_data = forms.cleaned_data.copy()
            news_data['author'] = author
            news = News.objects.create(**news_data)
            news.categories.set(category)
            return redirect('home-page')
    context = {"forms": forms}
    return render(request, 'news_form.html', context)
