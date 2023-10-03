from rest_framework import serializers
from .models import Product, Review, Blog, Search


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = "__all__"
    

