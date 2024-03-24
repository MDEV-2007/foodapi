from rest_framework import generics
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category_list'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category_id']



class ProductDetailCustom(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



@api_view(['GET','POST'])
def api_product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)
