from django.db import models
from django.utils import timezone

from django.forms import ModelForm

# Create your models here.
class Verb(models.Model):
	CONJUGATION_CHOICES = (
		("Indicative present", "Indicative present"),
		("Indicative imperfect", "Indicative imperfect"),
		("Indicative past", "Indicative past"),
		("Indicative future", "Indicative future"),
		("Conditional present", "Conditional present"),
		("Subjunctive present", "Subjunctive present"),
		("Subjunctive imperfect", "Subjunctive imperfect"),
		("Imperative", "Imperative"),
	)
	english_infinitive = models.CharField(max_length = 100)
	italian_conjugation = models.CharField(max_length = 100, choices=CONJUGATION_CHOICES)
	italian_infinitive = models.CharField(max_length = 100)
	italian_io = models.CharField(max_length = 100, blank=True)
	italian_tu = models.CharField(max_length = 100)
	italian_lei = models.CharField(max_length = 100)
	italian_noi = models.CharField(max_length = 100)
	italian_voi = models.CharField(max_length = 100)
	italian_essi = models.CharField(max_length = 100)
	publication_date = models.DateTimeField('date published', default = timezone.now())

	def __unicode__(self):
		return self.english_infinitive + " " + self.italian_infinitive

class VerbForm(ModelForm):
	class Meta:
		model = Verb
		fields = ['english_infinitive', 'italian_infinitive', 'italian_conjugation',
				'italian_io', 'italian_tu', 'italian_lei',
				'italian_noi', 'italian_voi', 'italian_essi']