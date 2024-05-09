from django.db import models
from django.utils import timezone
from home.models import medicine, Profile
from django.contrib.auth.models import User
from PIL import Image


class Bill(models.Model):
    customer_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class BillItem(models.Model):
    item = models.ForeignKey(medicine, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
