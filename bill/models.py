from django.db import models


class Owner(models.Model):
    from_name = models.CharField(max_length=126)
    from_address = models.CharField(max_length=126)
    from_pin = models.IntegerField()
    from_gst = models.CharField(max_length=126)


class Customer(models.Model):
    to_name = models.CharField(max_length=126)
    to_address = models.CharField(max_length=126)
    to_pin = models.IntegerField()
    to_gst = models.CharField(max_length=126)


