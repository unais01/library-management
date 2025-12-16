from rest_framework import serializers 
from .models import Book, Author, Category, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publishers_id = PublisherSerializer()
    category_id = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publishers_id')
        category_data = validated_data.pop('category_id')

        author, _ = Author.objects.get_or_create(**author_data)
        publisher, _ = Publisher.objects.get_or_create(**publisher_data)
        category, _ = Category.objects.get_or_create(**category_data)

        book = Book.objects.create(author=author, publishers_id=publisher, category_id=category, **validated_data)
        return book
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        publisher_data = validated_data.pop('publishers_id', None)
        category_data = validated_data.pop('category_id', None)

        if author_data:
            author, _ = Author.objects.get_or_create(**author_data)
            instance.author = author
        if publisher_data:
            publisher, _ = Publisher.objects.get_or_create(**publisher_data)
            instance.publishers_id = publisher
        if category_data:
            category, _ = Category.objects.get_or_create(**category_data)
            instance.category_id = category
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    