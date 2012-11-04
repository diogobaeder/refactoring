from nose.tools import istest
from unittest import TestCase

from refactoring.refactoring.introduceparameterobject import OrderService


class OrderServiceTest(TestCase):
    @istest
    def manages_the_order_received(self):
        service = OrderService()

        service.make_order({
            'product': 'TV',
            'user': 'John',
            'amount': 999.90,
        })

        self.assertEqual(service.orders, [{
            'product': 'TV',
            'user': 'John',
        }])
        self.assertEqual(service.transactions, [{
            'user': 'John',
            'amount': 999.90,
        }])