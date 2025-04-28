from rest_framework import viewsets, generics
from .models import Book, Order
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
    OrderListSerializer,
    OrderDetailSerializer
)

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return OrderDetailSerializer
