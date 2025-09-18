from django.shortcuts import render
from .serializers import  CartItemSerializer,CartSerializer,CategorySerializer,CartstatSerializer,ProductDetailSerializer,ProductListSerializer, CategoryDetailSerializer,CategoryListSerializer
from .models import Product,Cart,CartItem,Category
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# Retourner une liste  des produits 
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products,many=True)
    return Response(serializer.data)

# Retourner une liste detail de produit
# pour avoir le detail du produit comme methode il fqut utiliser 
# objects.get()
@api_view(['GET'])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)



# Retourner la list de category de produits
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


# Retourner un detail de category
@api_view(['GET'])
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)


