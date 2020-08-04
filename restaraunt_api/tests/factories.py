import random

import factory
from django.contrib.auth import get_user_model
from restaraunt_api.models import Order, Company, Product


class ProductFactory(factory.django.DjangoModelFactory):
    sku = factory.Sequence(lambda n: 'sku_%d' % n)
    name = factory.Sequence(lambda n: 'sku_%d' % n)
    price = factory.lazy_attribute(lambda o: random.randint(10, 1000))

    class Meta:
        model = Product


class CompanyFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'company_%d' % n)

    class Meta:
        model = Company


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    company = factory.RelatedFactory(CompanyFactory, 'company')
    products = factory.RelatedFactory(ProductFactory, 'product')

    # noinspection PyUnusedLocal
    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.add(product)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
