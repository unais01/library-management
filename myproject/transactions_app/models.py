from django.db import models
from users_app.models import User

# Create your models here.

class Transactions(models.Model):
    book = models.ForeignKey('library.Book', on_delete=models.CASCADE, related_name='transactions')
    issued_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='issued_transactions')
    issue_date = models.DateField(null=True, blank=True)
    return_before = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(max_length=500, blank=True)    


    def __str__(self):
        return f"Transaction for {self.book.title}"
    
class RequestedBooks(models.Model):
    book = models.ForeignKey('library.Book', on_delete=models.CASCADE, related_name='requested_books')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_requested_books')
    request_date = models.DateField(auto_now_add=True )
    




    