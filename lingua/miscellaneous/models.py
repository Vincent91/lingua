from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Misc(models.Model):
	english_phrase = models.CharField('english', max_length = 100)
	italian_phrase = models.CharField('italian', max_length = 100)
	publication_date = models.DateTimeField('date published', default = timezone.now())

	def __unicode__(self):
		return self.english_phrase + " " + self.italian_phrase

class MiscForm(ModelForm):
	class Meta:
		model = Misc
		fields = ['english_phrase', 'italian_phrase']