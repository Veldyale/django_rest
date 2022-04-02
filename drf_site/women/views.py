from rest_framework import generics
from django.shortcuts import render
from .models import Women, Category
from .serializers import WomenSerializer, CategorySerializer


# Create your views here.
class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
