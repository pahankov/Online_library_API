from rest_framework import serializers
from .models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    orders_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_orders_count(self, obj):
        return obj.order_set.count()


class OrderSerializer(serializers.ModelSerializer):
    # Для записи используем PrimaryKeyRelatedField
    books = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Book.objects.all(),
        write_only=True,  # Только для ввода, не для вывода
        required=True
    )

    # Для чтения используем BookSerializer
    book_details = BookSerializer(
        source='books',
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'user_name',
            'days_count',
            'date',
            'books',  # Для ввода (ID книг)
            'book_details'  # Для вывода (полные данные книг)
        ]
        extra_kwargs = {
            'books': {'required': True}
        }

    def to_representation(self, instance):
        """Переопределяем вывод, чтобы сохранить вашу логику"""
        representation = super().to_representation(instance)

        # Ваша существующая логика
        if 'list' in self.context.get('view_action', ''):
            representation['books'] = BookSerializer(
                instance.books.all(),
                many=True
            ).data

        # Удаляем дублирование данных
        representation.pop('book_details', None)
        return representation