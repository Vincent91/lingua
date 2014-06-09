from django.db import models
from django.utils import timezone

# Create your models here.
class Verb(models.Model):
	english_infinitive = models.CharField(max_length = 100)
	italian_conjugation = models.CharField(max_length = 100)
	italian_infinitive = models.CharField(max_length = 100)
	italian_io = models.CharField(max_length = 100)
	italian_tu = models.CharField(max_length = 100)
	italian_lei = models.CharField(max_length = 100)
	italian_noi = models.CharField(max_length = 100)
	italian_voi = models.CharField(max_length = 100)
	italian_essi = models.CharField(max_length = 100)
	publication_date = models.DateTimeField('date published', default = timezone.now())

	def __unicode__(self):
		return self.english_infinitive + " " + self.italian_infinitive

