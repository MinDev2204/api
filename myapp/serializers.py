from rest_framework import serializers
from .models import User, Product, Category

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)  # required=False qo'shildi
    userName = serializers.CharField(source='user.userName', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'user', 'userName', 'image', 'name', 'description', 'price', 'status']
        extra_kwargs = {
            'image': {'required': False},  # Bu ham ishlaydi
            'status': {'required': False}  # Agar kategoriya ham majburiy bo'lmasa
        }

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
        extra_kwargs = {
            'password': {'write_only': True}  # Parolni faqat yozish uchun qilish
        }
