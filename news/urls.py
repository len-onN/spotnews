from django.urls import path, include
from rest_framework import routers
from news_rest.views.category_view import CategoryViewSet
from news_rest.views.news_view import NewsViewSet
from news_rest.views.user_view import UserViewSet
from news.views import home, news_details, category_forms, new_news_forms

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", category_forms, name="categories-form"),
    path("news/", new_news_forms, name="news-form")
]
