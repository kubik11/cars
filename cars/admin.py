from django.contrib import admin
from .models import Team
from django.utils.html import format_html # In order to append html tag in admin
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
	def thambnail(self, object):
		return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))
	thambnail.short_description = "Photo"
	#fields amount set
	list_display = ("id", "thambnail", "first_name", "desingnition", "created_date")
	#clickable fields amount 
	list_display_links = ("id", "thambnail", "first_name")
	#search field
	search_fields = ("first_name", "last_name", "desingnition")
	#list filter by keywords
	list_filter = ('desingnition',)


admin.site.register(Team, TeamAdmin)