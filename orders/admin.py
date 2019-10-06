from django.contrib import admin

from .models import ItemPricing, Topping, MenuItems, menuCateg, Items, Orders
# Register your models here.

admin.site.register(ItemPricing)
admin.site.register(Topping)
admin.site.register(MenuItems)
admin.site.register(menuCateg)
admin.site.register(Items)
admin.site.register(Orders)
# admin.site.register(Customer)
