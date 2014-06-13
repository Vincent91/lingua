from django.contrib import admin
from miscellaneous.models import Misc

class MiscAdmin(admin.ModelAdmin):
	list_display = ('english_phrase', 'italian_phrase', 'publication_date')
	list_filter = ['publication_date']
	search_fields = ['english_phrase']

# Register your models here.
admin.site.register(Misc, MiscAdmin)