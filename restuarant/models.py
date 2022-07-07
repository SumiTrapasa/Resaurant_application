from django.db import models

import restuarant

# Create your models here.
class Restuarant(models.Model):
    name = models.CharField(max_length=120)
    discriptions = models.TextField(blank=True, null=True)
    location = models.TextField(blank=False, null=False)
    cuisines = models.ManyToManyField("cuisines", related_name="restuarants")
    veg_type = models.TextField(max_length=10, choices=(('veg','veg'), ('non-veg','non-veg')), default="1")
    rating = models.FloatField()
    contact =models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Cuisines(models.Model):
    cuisines_type = models.CharField( max_length=120)

    def __str__(self):
        return self.cuisines_type

class Menu (models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField(blank=True, null=True)
    cuisines_type = models.ForeignKey("cuisines",on_delete=models.CASCADE, related_name="cuisine")
    price = models.IntegerField()
    veg_type = models.TextField(max_length=10, choices=(('veg','veg'), ('non-veg','non-veg')), default="1")
    rname= models.ForeignKey("Restuarant", on_delete=models.CASCADE, default="1", related_name="menu_items")

    def __str__(self):
        return self.name

