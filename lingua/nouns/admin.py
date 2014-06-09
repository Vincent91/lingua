from django.contrib import admin
from nouns.models import Noun

class NounAdmin(admin.ModelAdmin):
	fieldsets = [
		('English', {'fields': ['english_single']}),
		('Italian single', {'fields': ['italian_single_article', 'italian_single']}),
		('Italian plural', {'fields': ['italian_plural_article', 'italian_plural']}),
	]
	list_display = ('english_single', 'italian_single_method', 'italian_plural_method', 'publication_date')
	list_filter = ['publication_date']
	search_fields = ['english_single']

# Register your models here.
admin.site.register(Noun, NounAdmin)