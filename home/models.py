from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Insurance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=100)
    provider_name = models.CharField(max_length=100)
    holder_name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default="2025-02-09")

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="UserImages\default.jpg", upload_to="UserImages/")
    displayName = models.CharField(default="User", max_length=100)
    Date_of_Birth = models.DateField(default="2000-01-01")
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]
    bloodGroup = models.CharField(
        choices=BLOOD_GROUP_CHOICES, max_length=3, default="O+"
    )
    phone = models.CharField(max_length=15, default="+1234567890")
    TempAddress = models.TextField(default="Temporary Address")
    PermanentAddress = models.TextField(default="Permanent Address")
    USER_TYPE_CHOICES = [
        ("Customer", "Customer"),
        ("Worker", "Worker"),
        ("Owner", "Owner"),
        ("Admin", "Admin"),
    ]
    user_type = models.CharField(
        choices=USER_TYPE_CHOICES, max_length=10, default="Customer"
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)
