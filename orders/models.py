from django.db import models
from django.contrib.auth.models import User


SIZES = (
    ("s", "Small"),
    ("l", "Lagre"),
)

TYPES = (
    ("r", "Regular"),
    ("s", "Sicilian"),
)

# Create your models here.
class ItemPricing(models.Model):
    """docstring for menu Item Pricing."""

    item_type = models.CharField(max_length=1, choices=TYPES)
    item_size = models.CharField(max_length=1, choices=SIZES)
    num_topping = models.IntegerField()
    item_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return ("{} {} with {} = ${}".format(self.item_size, self.item_type, self.num_topping, self.item_price))

class Topping(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return ("{}".format(self.name))


class MenuItems(models.Model):

    name = models.CharField(max_length=1, choices=TYPES)
    size = models.CharField(max_length=1, choices=SIZES)
    price = models.ForeignKey(ItemPricing, on_delete=models.CASCADE, related_name="pizza_price")
    topping = models.ManyToManyField(Topping, blank=True, related_name="pizza_topping")


    def __str__(self):
        return ("[{}] [{}]".format(self.name, self.size))

class menuCateg(models.Model):

    name = models.CharField(max_length=64, blank=False)
    image = models.ImageField(upload_to="images/", default="pizza-1.jpg")

    def __str__(self):
        return ("{}".format(self.name,))


class Items(models.Model):
    """docstring for sub."""
    name = models.CharField(max_length=64, blank=False)
    smPrice = models.DecimalField(max_digits=5, decimal_places=2)
    lgPrice = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    menuCateg = models.ForeignKey(menuCateg, blank=True, on_delete=models.CASCADE, related_name="categ_item")
    image = models.ImageField(upload_to="images/items", default="pizza-1.jpg")

    def __str__(self):
        return ("{} small: {}$ and large: {}$ and Categ: {}".format(self.name, self.smPrice, self.lgPrice, self.menuCateg))

class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_name",default=1)
    menu = models.ForeignKey(menuCateg, on_delete=models.CASCADE, related_name='menu_categ', null=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='items', null=True)
    itemsize = models.CharField(max_length= 1, choices=SIZES, default="s")
    # total = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    ordered = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0)

    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return ("{} {} {} {} {} {} {}".format(self.customer, self.menu, self.item, self.ordered, self.finished, self.date, self.price))

# class Customer(models.Model):
#
#
#     orders = models.ManyToManyField(Orders, blank=True)
#
#     def __str__(self):
#         return ("{}".format(self.customer))
