from django.urls import path
from less_2 import views


urlpatterns = [
    path('index/', views.index, name='index-view'),
    path('bio/<username>/', views.bio, name='bio'),
    path('article/2023/', views.article_case_2023),
    path('article/<int:year>/', views.year_archive),
]
