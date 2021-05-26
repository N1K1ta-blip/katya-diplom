from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from cart.models import Cart, Item

@admin.register(Cart)
class CartAdmin(GuardedModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(GuardedModelAdmin):
    pass
