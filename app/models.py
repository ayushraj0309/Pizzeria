from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=255)

class Pizza(models.Model):
    BASE_CHOICES = [
        ('thin-crust', 'Thin Crust'),
        ('normal', 'Normal'),
        ('cheese-burst', 'Cheese Burst'),
    ]
    CHEESE_CHOICES = [
        ('mozzarella', 'Mozzarella'),
        ('cheddar', 'Cheddar'),
        ('parmesan', 'Parmesan'),
        ('gouda', 'Gouda'),
    ]

    name = models.CharField(max_length=255)
    base = models.CharField(max_length=15, choices=BASE_CHOICES)
    cheese = models.CharField(max_length=15, choices=CHEESE_CHOICES)
    toppings = models.ManyToManyField(Topping)

class Order(models.Model):
    STATUS_CHOICES = [
        ('Placed', 'Placed'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]

    pizzas = models.ManyToManyField(Pizza)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Placed')
