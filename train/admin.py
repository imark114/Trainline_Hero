from django.contrib import admin
from .models import SourceStation, DestinationStation, Train

# Register your models here.
admin.site.register(SourceStation)
admin.site.register(DestinationStation)

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ['name', 'source', 'destination']

    def source(self, obj):
        return obj.source_station.name

    def destination(self, obj):
        return obj.destination_station.name
