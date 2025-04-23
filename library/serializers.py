from rest_framework import serializers
from .models import Book, Order


# Сериализатор для списка книг (минимум информации)
class BookListSerializer(serializers.ModelSerializer):
    orders_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year', 'orders_count']

    def get_orders_count(self, obj):
        return obj.order_set.count()


# Сериализатор для деталей книги (полная информация)
class BookDetailSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_orders(self, obj):
        return obj.order_set.values_list('id', flat=True)


# Сериализатор для списка заказов
class OrderListSerializer(serializers.ModelSerializer):
    book_titles = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user_name', 'days_count', 'date', 'book_titles']

    def get_book_titles(self, obj):
        return [book.title for book in obj.books.all()]


# Сериализатор для деталей заказа
class OrderDetailSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True, read_only=True)

    # Для ввода используем PrimaryKeyRelatedField
    book_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Book.objects.all(),
        source='books',
        write_only=True,
        required=True
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'user_name',
            'days_count',
            'date',
            'books',  # полная информация (только для чтения)
            'book_ids'  # только ID (только для записи)
        ]
