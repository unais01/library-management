from django.urls import path
from library.views import BookDetailView, BookListView
# from transactions_app.views import transaction_list
from users_app.views import UserRegistrationView, UserProfileView, UsersListView, UserDetailView
from transactions_app.views import TransactionListView, ReturnBookView, IssueBookView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('books/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='booksView-list'),
 
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/', UsersListView.as_view() , name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
                                                
    path('issue/', IssueBookView.as_view(), name='issue-book'),
    path('transactions/', TransactionListView.as_view(), name='my-transaction'),
    path('mybooks/', TransactionListView.as_view(), name='my-books'),
    path('return/<int:id>/', ReturnBookView.as_view(), name='return-book'),
]

