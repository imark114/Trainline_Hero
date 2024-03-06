from django.db import models
from .constant import SOURCE_STATIONS, DESTINATION_STATIONS
# Create your models here.
class SourceStation(models.Model):
    name = models.CharField(max_length=15, choices=SOURCE_STATIONS)
    def __str__(self):
        return self.name
    

class DestinationStation(models.Model):
    name = models.CharField(max_length=15, choices=DESTINATION_STATIONS)
    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=20)
    source_station = models.ForeignKey(SourceStation,on_delete=models.CASCADE, related_name='source')
    destination_station = models.ForeignKey(DestinationStation, on_delete=models.CASCADE, related_name='destination')
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField(default=total_seats) 
    ticket_price = models.DecimalField(decimal_places=2, max_digits=12,blank=True, null=True)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name
    