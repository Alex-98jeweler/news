from django.urls import path

from . import views


urlpatterns = [
    path('', views.news_list, name='index'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('create/', views.create, name='news-create'),
    path('<int:pk>/delete/', views.NewsDelete.as_view(), name='news-delete')
]
