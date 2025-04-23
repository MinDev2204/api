from rest_framework import serializers
from .models import User, Product, Category

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    userName = serializers.CharField(source='user.userName', read_only=True)

    class Meta:
        model = Product
        fields = ['user', 'userName', 'image', 'name', 'description', 'price', 'status']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'userName', 'password', 'products', 'categories']
