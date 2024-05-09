import os

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Pizza, Topping, Order


class PizzaOrderTestCase(TestCase):
    def setUp(self):
        super(PizzaOrderTestCase, self).setUp()
        self.client = APIClient()

    def create_pizza(self, name, base, cheese, toppings):
        return Pizza.objects.create(name=name, base=base, cheese=cheese, toppings=toppings)

    def test_create_pizza_order(self):
        # Create some toppings
        topping1 = Topping.objects.create(name='Pepperoni')
        topping2 = Topping.objects.create(name='Mushrooms')

        # Create a pizza
        pizza = self.create_pizza(name='Pepperoni Pizza', base='thin-crust', cheese='mozzarella',
                                  toppings=[topping1, topping2])

        # Create an order with the pizza
        order_data = {
            'pizzas': [pizza.id],
            'status': 'Placed'
        }
        response = self.client.post(reverse('order-list'), order_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().pizzas.count(), 1)
        self.assertEqual(Order.objects.get().pizzas.first().name, 'Pepperoni Pizza')
