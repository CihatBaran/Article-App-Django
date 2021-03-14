from django.contrib import admin
from django.urls import path
from article.views import dashboard, add_article, ind_article, ind_article_edit, ind_article_delete

app_name = "article"

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/<int:id>', ind_article, name="ind_article"),
    path('dashboard/edit/<int:id>', ind_article_edit, name="ind_article"),
    path('dashboard/delete/<int:id>', ind_article_delete, name="ind_article"),
    path('add-article/', add_article, name="article_add"),
    path('mainpage', add_article, name="main_page_article")

]
