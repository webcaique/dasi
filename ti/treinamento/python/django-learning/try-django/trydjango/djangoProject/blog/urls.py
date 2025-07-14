from django.contrib import admin
from django.urls import path

from .views import (
    article_list_view,
    article_details_view,
    article_update_view,
    article_delete_view,
    article_create_view
)
   
app_name = 'articles' 
urlpatterns = [
    path('', article_list_view, name='articles-list'),
    path('<int:id>/', article_details_view, name="articles-details" ),
    path('<int:id>/update/', article_update_view, name="articles-update" ),
    path('<int:id>/delete/', article_delete_view, name="articles_delete"),
    path('create/', article_create_view, name="articles_create")
    
    
]