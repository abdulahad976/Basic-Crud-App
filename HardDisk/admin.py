from django.contrib import admin
from .models import Disk

# Register your models here.
@admin.register(Disk)
class HardDiskAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'price')
    list_display_links = ('name', 'capacity', 'price')
    