from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.


class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.URLField(blank=True ,null=True)


    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name



class Product(models.Model):
     name = models.CharField(max_length=100)
     category = models.ForeignKey(Category, on_delete=models.CASCADE,  null=True, blank=True)
     image = models.ImageField(upload_to='img', blank=True, null=True)
     description = models.TextField()
     slug = models.SlugField(unique=True, blank=True)
     price = models.DecimalField(max_digits=5, decimal_places=2)
     stock = models.IntegerField()


     def __str__(self):
            return f" Cart {self.name} for {self.email}" 
     
    #  une fonction pour cree un slug automatiquement 

     def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1

            # boucle tant qu'un slug identique existe déjà
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        # on sauvegarde toujours, même si le slug existe déjà
            super().save(*args, **kwargs)

        


    

class Cart(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE,  null=True, blank=True)
    cart_code  = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.cart_code} for {self.customer.name}"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # fonction pour claculer le sub total 
    # on prent le price et * la quantity 

    def sub_total(self):
        return self.price *  self.quantity
    

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    # une petite affichage :  5 x moringa






