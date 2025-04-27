from rest_framework import generics
from rest_framework import viewsets
from .models import Book, Order
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
    OrderListSerializer,
    OrderDetailSerializer
)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return OrderDetailSerializer
