from django.contrib import admin
from .models import Vehicle
from django.utils.html import format_html # In order to append html tag in admin

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
	def thambnail(self, object):
		return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.car_photo.url))
	thambnail.short_description = "Vehicle Photo"
	list_display = ('id', 'thambnail', 'car_title', 'city', 'model', 'year', 'price', 'is_featured')
	list_display_links = ('id', 'thambnail', 'car_title')
	search_fields = ("city", "car_title", "model", "year")
	list_editable = ('is_featured',) # Allow editing into the table


admin.site.register(Vehicle, VehicleAdmin) 