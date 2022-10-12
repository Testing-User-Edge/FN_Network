from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path("", PostListView.as_view(), name="Home Page"),
    path("user/<str:username>/", UserPostListView.as_view(), name="User Post Page"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="Post Page"),
    path("post/new/", PostCreateView.as_view(), name="Create Page"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="Update Page"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="Delete Page"),
    path("about/", views.about, name="About Page"),
]