from rest_framework import serializers
from . models import Product,Cart,CartItem,Category,CustomerUser
from django.contrib.auth import get_user_model


# pour le customer user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "profile_picture_url"]



# pour la liste des produits 
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'price', 'stock']


# pour le produit specifique 
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'description', 'image', 'category', 'price', 'stock']

# pour le category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']

# Pour la liste des category

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'image', 'slug']


# pour le detailcategory
class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'products']


# pour la cartitem
# c'est dans la meme class serializer qu'on le va cree des fonction 
# de calcul des total 
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    sub_total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['cart','product','quantity','price','created_at','updated_at']


        # on cree une fonction va retourner  le subtotal 
        #  qui prend en parmetrre le cartitem
        # cette fonction  multiplie le prix et la quantite
        def get_sub_total(self, cartitem):
            total = cartitem.product.price * cartitem.quantity
            return total

# pour le cart
# ici dans la class cart nous allons 
# calculer  le prix total de la carte 
class CartSerializer(serializers.ModelSerializer):
    cartitem = CartItemSerializer(read_only=True) 
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['customer', 'cart_code', 'created_at']
# avoir le total 
        def get_cart_total(self, cart):
            ps = cart.cartitem.all()
            total = sum([p.quantity *  p.product.price for  p in ps])

# c'est ici que nous allons calculer la quantite total 
class CartstatSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'cart_code','total_quantity']

    
    def get_total_quantity(self, cart):
        ps = cart.cartitem.all()
        total = sum([ps.quantity * p.product.price for p in ps])
        return total





