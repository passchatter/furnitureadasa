from django.db import models
from core.models import Produks
from django.contrib.auth.models import User

class CartItems(models.Model):
    produk = models.ForeignKey(Produks, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.produk.name



class OrderItem(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    produk = models.ForeignKey(Produks, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def subtotal(self):
        return self.produk.price * self.quantity

    def __str__(self):
        return str(self.username)
 