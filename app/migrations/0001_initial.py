# Generated by Django 3.1.6 on 2023-09-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('base', models.CharField(choices=[('thin-crust', 'Thin Crust'), ('normal', 'Normal'), ('cheese-burst', 'Cheese Burst')], max_length=15)),
                ('cheese', models.CharField(choices=[('mozzarella', 'Mozzarella'), ('cheddar', 'Cheddar'), ('parmesan', 'Parmesan'), ('gouda', 'Gouda')], max_length=15)),
                ('toppings', models.ManyToManyField(to='app.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Placed', 'Placed'), ('Accepted', 'Accepted'), ('Preparing', 'Preparing'), ('Dispatched', 'Dispatched'), ('Delivered', 'Delivered')], default='Placed', max_length=15)),
                ('pizzas', models.ManyToManyField(to='app.Pizza')),
            ],
        ),
    ]
