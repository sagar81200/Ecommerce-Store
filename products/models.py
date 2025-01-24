from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
