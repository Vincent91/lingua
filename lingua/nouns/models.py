from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Noun(models.Model):
	english_single = models.CharField(max_length = 100)
	italian_single = models.CharField(max_length = 100)
	italian_plural = models.CharField(max_length = 100)
	italian_single_article = models.CharField(max_length = 3)
	italian_plural_article = models.CharField(max_length = 3)
	publication_date = models.DateTimeField('date published', default = timezone.now())

	def italian_single_method(self):
		return self.italian_single_article + " " + self.italian_single
	italian_single_method.short_description = 'italian single'	

	def italian_plural_method(self):
		return self.italian_plural_article + " " + self.italian_plural
	italian_plural_method.short_description = 'italian plural'

	def __unicode__(self):
		return self.italian_single_article + " " + self.italian_single

class NounForm(ModelForm):
	class Meta:
		model = Noun
		fields = ['english_single', 'italian_single', 'italian_single_article', 'italian_plural', 'italian_plural_article']