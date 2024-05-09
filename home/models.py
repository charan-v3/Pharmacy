from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Insurance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=100)
    provider_name = models.CharField(max_length=100)
    holder_name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    def __str__(self):
        return self.policy_number


class medicine(models.Model):
    drugname = models.CharField(max_length=50, null=True)
    batchno = models.CharField(max_length=10, default="A1")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    medtype = models.CharField(max_length=50, default="Normal")
    manufacturer = models.CharField(max_length=50)
    stockqty = models.IntegerField(default=15)
    expirydate = models.DateField(default=timezone.now)
    description = models.TextField(max_length=100, default="Enter Description")
    img = models.ImageField(null=True, blank=True, upload_to="medicineImages/")

    def __str__(self):
        return self.drugname
