from django.contrib import admin
from .models import OrderItem, CartItems


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('username', 'create_at', 'produk', 'quantity', 'subtotal')  # Ganti 'other_field_name' dengan nama field lain yang ingin Anda tampilkan

admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(CartItems)