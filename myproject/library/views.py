
from .permissions import IsAdminOrReadOnly
from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
import django_filters



class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        django_filters.rest_framework.DjangoFilterBackend
    ]
    filterset_fields = ['title']

    search_fields = ['title']

    ordering_fields = ['title']
    
class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk' 
    permission_classes = [IsAdminOrReadOnly]   



         
