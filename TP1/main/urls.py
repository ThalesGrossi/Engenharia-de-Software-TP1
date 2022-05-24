from django.urls import path
from . import views
from .views import ArticleDetailView, AddCommentView, UpdatePostView, LikeView, LikeViewC

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('thread/<int:pk>', ArticleDetailView.as_view(), name='thread'),
    path('thread/<int:pk>/comment', AddCommentView.as_view(), name='create_comment'),
    path('thread/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('like/<int:pk>', LikeViewC, name='comment_post'),
]
