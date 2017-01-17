from django.db import models

# Create your models here.
class Cafe(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    local = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)
    lat = models.FloatField()
    lng = models.FloatField()

    wifi = models.BooleanField()
    plug = models.BooleanField()
    table = models.IntegerField()
    floor = models.CharField(max_length=5)

    time_killing = models.FloatField()
    reading_books = models.FloatField()
    studying = models.FloatField()
    web_surfing = models.FloatField()

    beverage = models.FloatField()
    dessert = models.FloatField()
    quiet = models.FloatField()
    kind = models.FloatField()

    score = models.FloatField()

    def __str__(self):
        return "{} ({})".format(self.name,self.tel)

class Survey(models.Model):
    cafe = models.ForeignKey(Cafe)

    wifi = models.BooleanField()
    plug = models.BooleanField()
    table = models.IntegerField()
    floor = models.CharField(max_length=5)

    time_killing = models.FloatField()
    reading_books = models.FloatField()
    studying = models.FloatField()
    web_surfing = models.FloatField()

    beverage = models.FloatField()
    dessert = models.FloatField()
    quiet = models.FloatField()
    kind = models.FloatField()

    status = models.BooleanField()
