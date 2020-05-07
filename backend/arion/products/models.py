from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        

class Product(models.Model):
    image = models.ImageField(upload_to='uploads/product/images/', blank=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    can_be_sold = models.BooleanField()
    internal_reference = models.CharField(max_length=64, blank=True)
    barcode = models.CharField(max_length=64, blank=True)
    price = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
