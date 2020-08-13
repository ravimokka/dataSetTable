from django.db import models


# Create your models here.


class CompanyInfo(models.Model):
    AmazonShipmentID = models.TextField(max_length=1000, blank=True, null=True)
    CompanyName = models.TextField(max_length=10000, blank=True, null=True)
    CreatedDate = models.TextField(max_length=10000, blank=True, null=True)
    PRONumber = models.TextField(max_length=10000, blank=True, null=True)
    ShipStatus = models.TextField(max_length=10000, blank=True, null=True)
    ShipStatusNum = models.IntegerField(blank=True, null=True)
    TotalCartons = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.AmazonShipmentID
