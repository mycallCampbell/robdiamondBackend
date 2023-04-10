from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Blog, Search, Order, OrderItem, ShippingAddress
from .serializer import ProductsSerializer, BlogsSerializer, SearchSerializer
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from functools import reduce


stripe.api_key = settings.STRIPE_PRIVATE_KEY


# Create your views here.
# For the reduce function


def prod(x, y):
    return x + y


def getRoutes(request):
    return JsonResponse('Rob Diamond API', safe=False)


@api_view(['GET'])
def getSearch(request):
    search = Search.objects.get(name=['name'])
    serializer = SearchSerializer(search, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getProductWatches(request):
    products = Product.objects.filter(category='watches')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductModelDateJust(request):
    products = Product.objects.filter(model='datejust')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductModelDayDate(request):
    products = Product.objects.filter(model='daydate')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductModelSkyDweller(request):
    products = Product.objects.filter(model='skydweller')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductModelDaytona(request):
    products = Product.objects.filter(model='daytona')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductModelGMTMASTERII(request):
    products = Product.objects.filter(model='GMT-MasterII')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductModelSubmariner(request):
    products = Product.objects.filter(model='submariner')
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBlogs(request):
    blogs = Blog.objects.filter(goLive='true')
    serializer = BlogsSerializer(blogs, many=True)
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


@api_view(['GET'])
def getBlog(request, pk):
    blog = Blog.objects.get(_id=pk)
    serializer = BlogsSerializer(blog, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def getClientSecret(request):

    productPriceList = []
    data = request.data
    for i in data:
        product = Product.objects.get(_id=i['_id'])
        productPriceList.append(product.price)
    productTotal = reduce(prod, productPriceList)
    global totalProduct
    totalProduct = round((productTotal * 100) + 299.00)

    try:
        intent = stripe.PaymentIntent.create(
            amount=totalProduct,
            currency='gbp',
            metadata={'integration_check': 'accept_a_payment'},
        )
        return JsonResponse({
            'client_secret': intent.client_secret
        })

    except:
        return Response({'Details': 'Server Error....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def addOrderItems(request):

    data = request.data

    shippingPrice = data["delivery"]
    if data and len(data) == 0:
        return Response({"Detail: No Items in the Cart"}, HttpResponse(status=400))
    else:
        if shippingPrice != "Standard":
            shippingPrice = 5.99
        else:
            shippingPrice = 2.99
        totalPrice = shippingPrice + totalProduct
        totalPrice = round(totalPrice, 2)

        order = Order.objects.create(
            shippingPrice=shippingPrice,
        )

        shipping = ShippingAddress.objects.create(
            order=order,
            addressLine1=data["deliveryDetails"]["addressLine1"],
            addressLine2=data["deliveryDetails"]["addressLine2"],
            city=data["deliveryDetails"]["city"],
            postcode=data["deliveryDetails"]["postcode"],
            shippingPrice=shippingPrice,
            phone=data["deliveryDetails"]["phone"],
        )

        for i in data["cartStorage"]:
            product = Product.objects.get(_id=i["_id"])

            OrderItem.objects.create(
                product=product,
                order=order,
                price=i["price"],
                name=product.name,
                size=i["size"],
                halfSize=i["halfSize"],
            )

            product.countInStock -= 1
            product.save()

    return HttpResponse(status=200)


@api_view(["POST"])
def sendEmail(request):
    # Convert List to String to comply with django Send_mail module
    s = [
        request.data["firstName"],
        request.data["sureName"],
        request.data["phone"],
        request.data["email"],
        request.data["message"],
    ]
    listToString = " ".join(map(str, s))
    # print(listToString)

    try:
        send_mail(
            "Contact Enquiry",
            listToString,
            "contact@robdiamond.co.uk",
            ["contact@robdiamond.co.uk"],
            fail_silently=False,
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    return Response("Success")


@api_view(["POST"])
def sendEmail(request):
    client = APIClient('your_app_key', 'your_app_key_cert_path')
