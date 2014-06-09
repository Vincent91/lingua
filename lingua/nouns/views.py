from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from nouns.models import Noun

# Create your views here.
def concrete_noun(request, noun_id):
	noun = get_object_or_404(Noun, pk = noun_id)
	return render(request, 'concrete_noun.html', {'noun': noun})

def all_nouns(request):
	nouns_list = Noun.objects.all()
	context = {'nouns_list': nouns_list}
	return render(request, 'all_nouns.html', context)