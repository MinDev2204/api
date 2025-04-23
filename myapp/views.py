from rest_framework import viewsets
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def perform_create(self, serializer):
        # Get the user from the request (you'll need to ensure your request is authenticated)
        # Or alternatively, get the user ID from the request data
        serializer.save(user_id=self.request.data.get('user'))