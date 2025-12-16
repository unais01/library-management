from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
       return self.category
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    publishers_id =models.ForeignKey(Publisher, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('available', 'Available'),
        # ('requested', 'Requested'),
        ('someone requested', 'Someone Requested'),
        ('not available', 'Not Available')
    ], default='available')



        
    
    def __str__(self):
        return f"{self.title} by {self.author}"

# Create your models here.
