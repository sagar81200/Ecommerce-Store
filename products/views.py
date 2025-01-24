from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    @action(detail=False, methods=['get'], url_path='expensive-product')
    def expensive_product(self, request):
        expensive_product = Product.objects.all().order_by("-price").first()
        serializer = ProductSerializer(expensive_product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'], url_path='update-stocks')
    def update_stock(self, request, pk=None):
        product = Product.objects.filter(pk=pk).first()
        if not product:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        stock = request.data.get("stock")
        if stock is not None:
            product.stock = stock
            product.save()
            return Response(
                {"message": "Stock updated successfully", "product_id": product.id, "new_stock": product.stock},
                status=status.HTTP_200_OK,
            )
        return Response({"detail": "Invalid stock value"}, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
