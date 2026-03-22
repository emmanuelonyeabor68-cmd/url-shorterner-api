from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, get_object_or_404
from rest_framework.generics import RetrieveAPIView

from .models import URL
from .serializers import URLSerializer
from .utils import generate_shortcode


# Create your views here.

class ShortenURLView(APIView):
    def post(self, request):
       serializer = URLSerializer(data=request.data)

       if serializer.is_valid():
            short_code = generate_shortcode()

            while URL.objects.filter(short_code=short_code).exists():
                short_code = generate_shortcode()
            url = serializer.save(short_code=short_code)
            return Response ({"original_url": url.original_url, "short_url": f"http://127.0.0.1:8000/{url.short_code}"},status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)

class URLStatsView(RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    lookup_field = "short_code"

 

