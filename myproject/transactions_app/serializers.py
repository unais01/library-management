from rest_framework import serializers
from .models import Transactions
from django.utils import timezone

class TransactionsSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_author = serializers.CharField(source='book.author.name', read_only=True)
    issued_to_username = serializers.CharField(source='issued_to.username', read_only=True)
    

    class Meta:
        model = Transactions
        fields = [
            'id',
            'book',
            'book_title',
            'book_author',
            'issued_to',
            'issued_to_username',
            'issue_date',
            'return_before',
            'return_date',
            'remarks'
        ]

class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'book',
            'issued_to',
            'issue_date',
            'return_before',
        ]
    def validate_book(self, value):
        if value.status != 'available':
            raise serializers.ValidationError("This book is not available for issuing.")
        return value
    def create(self, validated_data):
        if validated_data.get('issue_date') is None:
            validated_data['issue_date'] = timezone.now().date()
        if validated_data.get('return_before') is None:
            validated_data['return_before'] = validated_data['issue_date'] + timezone.timedelta(days=14)

        transaction = Transactions.objects.create(**validated_data)
        book = transaction.book
        book.status = 'not available'
        book.save()
        return transaction

class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'id',
            'return_date',
            'remarks'
        ]    
    def validate_return_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Return date cannot be in the future.")
        return value
    def update(self, instance, validated_data):
        return_date = validated_data.get('return_date')
        if return_date is None:
            return_date = timezone.now().date()
        
        instance.return_date = return_date
        instance.remarks = validated_data.get('remarks') or "No remarks provided"
        instance.save()

        book = instance.book
        book.status = 'available'
        book.save()

        return instance
    
