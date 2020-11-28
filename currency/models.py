from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=50)
    key	= models.CharField(max_length=5)

    def __str__(self):
        return self.key

class CurrencyFaits(models.Model):
    name = models.CharField(max_length=50)
    conversionFactor = models.FloatField(default=0.0)
    fromcurrency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="fromcurrency")
    tocurrency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="tocurrency")

    def __str__(self):
        return self.name