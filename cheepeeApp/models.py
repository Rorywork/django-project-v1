from django.db import models

# Create your models here.

class Cheepee(models.Model):
    productName = models.CharField(max_length=60, blank=False)
    productImageUrl = models.TextField()
    productPrice = models.CharField(max_length=15, blank=False)
    cheepeeName = models.CharField(max_length=60, blank=False)
    cheepeeImageUrl = models.TextField()
    cheepeePrice = models.CharField(max_length=15, blank=False)
    cheepeeInfo = models.CharField(max_length=60, blank=False)
    
    def __str__(self):	    
        return self.productName
        