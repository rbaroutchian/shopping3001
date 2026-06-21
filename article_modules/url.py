from django.urls import path
from . import views

urlpatterns=[
    path('',views.ArticleListView.as_view(),name='article-list'),
    path('<int:id>', views.ArticleDetailView.as_view(), name='article_detail'),

    path('add-article-comment/', views.add_article_comment, name='add_article_comment')

]
