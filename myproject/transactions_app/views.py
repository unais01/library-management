from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Transactions
from .serializers import ReturnBookSerializer, TransactionsSerializer, IssueBookSerializer
from rest_framework import status

from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView

class TransactionListView(ListAPIView):
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_student():
            return Transactions.objects.filter(issued_to=user)
        return Transactions.objects.all()

class ReturnBookView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ReturnBookSerializer
    queryset = Transactions.objects.filter(return_date__isnull=True)
    lookup_field = 'id'

class IssueBookView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = IssueBookSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transaction_list(request):
    if request.method == 'GET':
        if request.user.is_student():
            transactions = Transactions.objects.filter(issued_to=request.user)
        else:
            transactions = Transactions.objects.all()
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data) 
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def return_book(request, transaction_id):
    try:
        transaction = Transactions.objects.get(
            id=transaction_id, 
            return_date__isnull=True
        )
    except Transactions.DoesNotExist:
        return Response(
            {'error': 'Transaction not found or book already returned'}, 
            status=status.HTTP_404_NOT_FOUND
        )

    if request.user.is_student():
        return Response(
            {'error': 'You can only return books that you issued'},
            status=status.HTTP_403_FORBIDDEN
        ) 
    serializer = ReturnBookSerializer(transaction, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           

