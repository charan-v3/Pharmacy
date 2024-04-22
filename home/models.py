from django.db import models
from django.utils import timezone


class medicine(models.Model):
    drugname = models.TextField(max_length=50, null=True)
    batchno = models.CharField(max_length=10, default="A1")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    medtype = models.TextField(max_length=50)
    manufacturer = models.TextField(max_length=50)
    stockqty = models.IntegerField()
    expirydate = models.DateTimeField(default=timezone.now)
    img = models.ImageField(null=True, blank=True, upload_to="medicineImages/")

    def __str__(self):
        return self.drugname
