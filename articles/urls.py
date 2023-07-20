from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.Article.as_view()),
    re_path(r'fa/(?P<slug>[-\w]+)', views.ArticleDetails.as_view(),name='article-details')
]
