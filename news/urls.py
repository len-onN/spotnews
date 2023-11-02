from django.urls import path
from news.views import home, news_details, category_forms, new_news_forms

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", category_forms, name="categories-form"),
    path("news/", new_news_forms, name="news-form")
]
