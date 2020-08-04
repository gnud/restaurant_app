import pytest
from factory.django import DjangoModelFactory

from restaraunt_api.tests.factories import (
    OrderFactory,
    CompanyFactory, UserFactory, ProductFactory)


class TestOrders:
    @pytest.mark.django_db
    def test_order(self):
        """Tests that we can create products associated with a order."""

        company = CompanyFactory()
        order: DjangoModelFactory = OrderFactory(
            user=UserFactory(),
            company_id=company.pk,
            company=company,
            products=[ProductFactory()]
        )

        assert order.products.count() > 0
