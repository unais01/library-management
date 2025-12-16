from django.contrib import admin
from .models import Transactions, RequestedBooks


admin.site.register([Transactions, RequestedBooks])
# Register your models here.
