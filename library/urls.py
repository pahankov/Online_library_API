from django.urls import path, include  # Добавляем импорт include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, OrderViewSet

router = DefaultRouter()
# Для BookViewSet (который наследуется от viewsets.ViewSet)
router.register(r'books', BookViewSet, basename='book')
# Для OrderViewSet (который наследуется от viewsets.ModelViewSet)
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),  # Подключаем роутер
]