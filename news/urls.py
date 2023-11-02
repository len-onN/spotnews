from django.urls import path
from news.views import home, news_details, news_forms

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", news_forms, name="categories-form")
]
