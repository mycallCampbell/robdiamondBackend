from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('watches/', views.getProductWatches, name='product-watches'),
    path('watchesModelDateJust/', views.getProductModelDateJust,
         name='product-modelDateJust'),
    path('watchesModelDayDate/', views.getProductModelDayDate,
         name='product-modelDayDate'),
    path('watchesModelSkyDweller/', views.getProductModelSkyDweller,
         name='product-modelSkyDweller'),
    path('watchesModelDaytona/', views.getProductModelDaytona,
         name='product-modelDaytona'),
    path('watchesModelSubmariner/', views.getProductModelSubmariner,
         name='product-modelSubmariner'),
    path('watchesModelGMT-MasterII/', views.getProductModelGMTMASTERII,
         name='product-modelGMT-MasterII'),
    path('watchesModelAquanaut/', views.getProductModelAquanaut, name='product-modelAquanaut'),
    path('watchesModelNautilus/', views.getProductModelNautilus, name='product-modelNautilus'),
    path('reviews/', views.getReviews, name='reviews'),
    path('blogs/', views.getBlogs, name='blogs'),
    path('watchesSold/', views.getProductWatchesSold, name='product-watchesSold'),
    path('watch/<str:pk>', views.getWatch, name='watch'),
    path('blog/<str:pk>', views.getBlog, name='blog'),
    path("client-secret/", views.getClientSecret, name="client-secret"),
    path("addorder/", views.addOrderItems, name='addorder'),
    path("sendEmail/", views.sendEmail, name="sendEmail"),
]
