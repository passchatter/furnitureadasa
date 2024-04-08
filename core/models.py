from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name
    
class Produks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='produks')
    price = models.IntegerField()
    material = models.CharField(max_length=100)
    ukuran = models.CharField(max_length=100)
    warna = models.CharField(max_length=100)
    fitur = models.TextField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    descriptiondua = models.TextField()

    def __str__(self):
        return self.name

    def comment_count(self):
        comments = Comment.objects.filter(produk=self).count()
        return comments

class Comment(models.Model):
    produk = models.ForeignKey(Produks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)