from django.contrib import admin
from .models import Harvest, RulesHarvest 

class HarvestAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'description',
        'status',
        'equipament', 
    )

    

admin.site.register(Harvest)
admin.site.register(RulesHarvest)