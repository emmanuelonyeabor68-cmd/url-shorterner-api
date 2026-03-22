from django.urls import path
from .views import ShortenURLView, URLStatsView, redirect_url

urlpatterns = [
    path('shorten/', ShortenURLView.as_view()),
    path('stats/<str:short_code>/', URLStatsView.as_view()),
    path("<str:short_code>/", redirect_url),
]