from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer
from .models import Product

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer