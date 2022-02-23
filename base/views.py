from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# Create your views here.

def getRoutes(request):
    return JsonResponse('Rob Diamond API', safe=False)

@api_view(['GET'])
def getProductWatches(request):
    products = Product.objects.filter(category='watches')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductWatchesSold(request):
    products = Product.objects.filter(category='watchesSold')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWatch(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductsSerializer(product, many=False)
    return Response(serializer.data)
