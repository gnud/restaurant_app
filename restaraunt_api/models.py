from django.db import models
from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'company-{self.pk}'


class Menu(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'menu-{self.pk}'


class Product(models.Model):
    sku = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    menu = models.ManyToManyField(Menu)

    def __str__(self):
        return f'product-{self.pk}'


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'order-{self.pk}'
