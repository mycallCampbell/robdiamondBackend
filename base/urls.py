from django.urls import path
from . import views

urlpatterns  = [
    path('',views.getRoutes, name="routes"), 
    path('watches/', views.getProductWatches, name='product-wathces'),
    path('watchesSold/', views.getProductWatchesSold, name='product-wathcesSold'),
    path('watch/<str:pk>', views.getWatch, name='watch'),
]