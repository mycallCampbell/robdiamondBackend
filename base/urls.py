from django.urls import path
from . import views

urlpatterns  = [
    path('',views.getRoutes, name="routes"), 
    path('watches/', views.getProductWatches, name='product-watches'),
    path('watchesSold/', views.getProductWatchesSold, name='product-watchesSold'),
    path('watch/<str:pk>', views.getWatch, name='watch'),
    path("client-secret/", views.getClientSecret, name="client-secret"),
    path("addorder/", views.addOrderItems, name='addorder'),
]