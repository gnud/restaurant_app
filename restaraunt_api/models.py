from django.contrib.auth.models import PermissionsMixin, AbstractUser
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


# region Django overrides
class User(AbstractUser, PermissionsMixin):
    """
    Overriding tbe base user model to allow further customization
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
    """

    # Needed to override in order to generate unique constraints to avoid clash with auth app
    is_superuser = models.BooleanField(
        default=False,
        help_text='Designates that this user has all permissions without explicitly assigning them.',
        verbose_name='superuser status'
    )

    def __str__(self):
        """
        Just to change something
        """

        return f'{self.email} [+]'
# endregion
