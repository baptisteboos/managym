from django.contrib import admin

from .models import Athlete, Group, Event, Apparatus, TargetResult, TypeEvent, \
	Information, TypeInformation

admin.site.register(Athlete)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Apparatus)
admin.site.register(TargetResult)
admin.site.register(TypeEvent)
admin.site.register(Information)
admin.site.register(TypeInformation)