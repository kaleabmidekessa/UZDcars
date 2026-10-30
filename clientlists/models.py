from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

class Clients_List(models.Model):
    name = models.CharField(max_length = 120)
    phone_number = models.CharField(max_length = 15)
    desired_car = models.CharField(max_length = 100)
    max_budget = models.DecimalField(max_digits = 12, decimal_places =2, blank = True, null = True)
    notes = models.TextField(blank = True)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)