from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return JsonResponse({"status": "API is live"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include("shortener.urls")),
    path('', include("shortener.urls")),
]
