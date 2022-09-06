from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    # path('', hello_world, name='hello_world')  # function based view
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home')  # as_view() in case we use class based view
]
