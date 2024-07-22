from django.urls import path
#имортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('search/', NewsSearch.as_view(), name='search'),
    path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
]
