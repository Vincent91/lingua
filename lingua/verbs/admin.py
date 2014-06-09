from django.contrib import admin
from verbs.models import Verb

class VerbAdmin(admin.ModelAdmin):
	fieldsets = [
		('English', {'fields': ['english_infinitive']}),
		('Italian general', {'fields': ['italian_conjugation', 'italian_infinitive']}),
		('Italian single', {'fields': ['italian_io', 'italian_tu', 'italian_lei']}),
		('Italian plural', {'fields': ['italian_noi', 'italian_voi', 'italian_essi']}),
	]
	list_display = ('english_infinitive', 'italian_infinitive', 'italian_conjugation', 'publication_date')
	list_filter = ['publication_date']
	search_fields = ['english_infinitive', 'italian_infinitive']

# Register your models here.
admin.site.register(Verb, VerbAdmin)