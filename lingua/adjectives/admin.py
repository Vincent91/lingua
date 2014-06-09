from django.contrib import admin
from adjectives.models import Adjective

class AdjectiveAdmin(admin.ModelAdmin):
	fieldsets = [
		('English', {'fields': ['english']}),
		('Italian single', {'fields': ['italian_single_masculine', 'italian_single_feminine']}),
		('Italian plural', {'fields': ['italian_plural_masculine', 'italian_plural_feminine']}),
	]
	list_display = ('english', 'italian_single_masculine', 'italian_plural_masculine', 'publication_date')
	list_filter = ['publication_date']
	search_fields = ['english']

# Register your models here.
admin.site.register(Adjective, AdjectiveAdmin)