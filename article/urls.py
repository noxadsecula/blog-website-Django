from django.contrib import admin
from django.urls import path
from .views import dashboard,addArticles,deleteArticle,updateArticle,detailView,articles,addComment


urlpatterns = [
    path("",articles,name="articles"),
    path("dashboard/", dashboard, name="dashboard"),
    path("addarticles/",addArticles, name="addarticles"),
    path("update/<int:id>",updateArticle, name="update"),
    path("delete/<int:id>",deleteArticle,name="delete"),
    path("article/<int:id>",detailView,name="detail"),
    path("comment/<int:id>",addComment, name="comment"),
    
]