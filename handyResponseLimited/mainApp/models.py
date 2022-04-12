import email
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Blog(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title
    
    
class ServiceForm:
    full_name = models.TextField(max_length=200)
    email = models.EmailField(max_length=245)
    phone_number = PhoneNumberField()
    
    

    