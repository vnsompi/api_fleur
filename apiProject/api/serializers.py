from rest_framework import serializers
from . models import Product,Cart,CartItem,Category,CustomerUser
from django.contrib.auth import get_user_model


# pour le customer user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "profile_picture_url"]

# pour le category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']

# pour la liste des produits 
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'price', 'stock']


# pour le produit specifique 
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name', 'description', 'image', 'category', 'price', 'stock']


# pour le cart
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['customer', 'cart_code', 'created_at']



# pour la cartitem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart','product','quantity','price','created_at','updated_at']
