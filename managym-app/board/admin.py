from django.contrib import admin

from .models import Athlete, Group, Event, Apparatus, TypeEvent, \
	Information, TypeInformation

class InformationInline(admin.TabularInline):
	model = Information
	extra = 0

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
	# radio_fields = {"gender": admin.HORIZONTAL}
	fields = (('gender', 'group'), ('first_name', 'last_name', 'birth_date'),\
		('email', 'email_2'), ('phone_number', 'phone_number_2'),\
		('address', 'city', 'province', 'postal_code')  )
	list_display = ['first_name', 'last_name', 'gender', 'birth_date', 'phone_number', 'email', 'group']
	list_display_links = ['first_name', 'last_name']
	list_filter = ['group', 'gender']
	search_fields = ['first_name', 'last_name']
	ordering = ['last_name', 'first_name']
	inlines = [InformationInline]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name', 'place', 'date'), 'description', 'type')
	list_display = ['name', 'place', 'date', 'type']
	list_filter = ['date']
	ordering = ['-date']


@admin.register(Apparatus)
class ApparatusAdmin(admin.ModelAdmin):
	fields = (('name', 'short_name'),)
	list_display = ['name', 'short_name']
	ordering = ['id']


class AthleteInline(admin.TabularInline):
	model = Athlete
	extra = 0

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	fields = (('name', 'trainers'),)
	inlines = [AthleteInline]
	ordering = ['name']

admin.site.register(TypeEvent)
admin.site.register(Information)
admin.site.register(TypeInformation)