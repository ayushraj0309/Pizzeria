from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet, ToppingViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
router.register(r'toppings', ToppingViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
