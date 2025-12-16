from django.urls import path
from library.views import BookDetailView, BookListView
# from transactions_app.views import transaction_list
from users_app.views import UserRegistrationView, CustomAuthToken, LogoutView, UserProfileView, UsersListView, UserDetailView
from transactions_app.views import TransactionListView, ReturnBookView, IssueBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='booksView-list'),
 
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/', UsersListView.as_view() , name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
                                                
    path('issue/', IssueBookView.as_view(), name='issue-book'),
    path('transactions/', TransactionListView.as_view(), name='my-transaction'),
    path('mybooks/', TransactionListView.as_view(), name='my-books'),
    path('return/<int:id>/', ReturnBookView.as_view(), name='return-book'),
]

