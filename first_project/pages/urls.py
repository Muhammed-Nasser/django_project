from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path('', hello_world, name='hello_world')  # function based view
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')  # as_view() in case we use class based view
]
