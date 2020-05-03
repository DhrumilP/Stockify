from django.db import models

class Stocks(models.Model):
    symbol = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    change = models.CharField(max_length=200)
    percent_change = models.CharField(max_length=200)
    market_caps = models.CharField(max_length=200, blank=True)
    avg_volume = models.CharField(max_length=200, blank=True)
    volume = models.CharField(max_length=200, blank=True)
