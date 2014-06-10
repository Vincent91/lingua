from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Adjective(models.Model):
	english = models.CharField(max_length = 100)
	italian_single_masculine = models.CharField(max_length = 100)
	italian_single_feminine = models.CharField(max_length = 100)
	italian_plural_masculine = models.CharField(max_length = 100)
	italian_plural_feminine = models.CharField(max_length = 100)
	publication_date = models.DateTimeField('date published', default = timezone.now())

	def __unicode__(self):
		return self.english + " " + self.italian_single_masculine


class AdjectiveForm(ModelForm):
	class Meta:
		model = Adjective
		fields = ['english', 'italian_single_masculine', 'italian_single_feminine', 
				  'italian_plural_masculine', 'italian_plural_feminine']
