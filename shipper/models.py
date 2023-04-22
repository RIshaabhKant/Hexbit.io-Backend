from django.db import models

class ShipperManager(models.Manager):
    def create_shipper(self, type: int, companyName: str, trackingUrl=None, urlStatus=None, checkPoints=None, totalCheckPoints=None, currentCheckPoint=None):
        shipper = self.model(type=type, companyName=companyName, trackingUrl=trackingUrl, urlStatus=urlStatus, checkPoints=checkPoints, totalCheckPoints=totalCheckPoints, currentCheckPoint=currentCheckPoint)
        return self.save(shipper=shipper)
    
    def save(self, shipper):
        shipper.save(using=self._db)
        return shipper

class Shipper(models.Model):
    type = models.SmallIntegerField()
    companyName = models.CharField(max_length=255)

    trackingUrl = models.CharField(max_length=255, unique=True, null=True)
    urlStatus = models.SmallIntegerField(null=True)
    checkPoints = models.JSONField(null=True)
    totalCheckPoints = models.SmallIntegerField(null=True)
    currentCheckPoint = models.SmallIntegerField(null=True)

    object = ShipperManager()

    def __str__(self):
        shipperVis = f'type: {self.type}, companyName: {self.companyName}'
        return shipperVis
