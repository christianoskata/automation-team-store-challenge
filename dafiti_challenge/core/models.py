from django.db import models


class Shoes(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    ref = models.CharField(max_length=15)
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    size = models.IntegerField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    weight = models.FloatField(blank=True, null=True)
    net_price = models.FloatField(null=False, blank=False)
    tax = models.FloatField(null=False, blank=False, default=5.00)
    gross_price = models.FloatField(null=False, blank=False)

    class Meta:
        ordering = ['-brand']
        verbose_name_plural = 'shoes'
        verbose_name = 'shoe'

    def __str__(self):
        return f'{self.name} - {self.brand}'
