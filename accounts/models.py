from django.db import models

from sre_constants import CATEGORY
from unicodedata import category
from attr import fields
from datetime import date
from django.contrib.auth.models import User
import uuid
# Create your models here.

# def upload_path(instance, filename):
#     filename = str(date.today())
#     name = instance.user.customer.public_id.hex
#     return f'{name}/platformLogo/{filename}.jpg'


class Customer(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    user = models.OneToOneField(User, null=True, blank =True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200, null=True)
    otp_code = models.CharField(max_length=6, null=True)
    phone = models.CharField(max_length=200, null=True)
    # profile_pic= models.ImageField(upload_to=upload_path, default='logo.png', null=True, blank=False,)
    
    
    def __str__(self):
        return self.name
