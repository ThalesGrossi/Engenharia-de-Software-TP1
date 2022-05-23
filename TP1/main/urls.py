from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('thread/<int:pk>', ArticleDetailView.as_view(), name='thread'),
]
