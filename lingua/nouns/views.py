from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from nouns.models import Noun, NounForm

# Create your views here.
def concrete_noun(request, noun_id):
	noun = get_object_or_404(Noun, pk = noun_id)
	return render(request, 'concrete_noun.html', {'noun': noun,})

def all_nouns(request):
	if request.method == 'POST':
		form = NounForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = NounForm()
	nouns_list = Noun.objects.all()
	context = {'nouns_list': nouns_list, 'form': form}
	return render(request, 'all_nouns.html', context)