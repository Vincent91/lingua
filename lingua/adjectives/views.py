from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from adjectives.models import Adjective, AdjectiveForm

# Create your views here.
def all_adjectives(request):
	if request.method == "POST":
		form = AdjectiveForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('')
	else:
		form = AdjectiveForm()
	adjectives_list = Adjective.objects.all()
	context = {'adjectives_list': adjectives_list, 'form': form}
	return render(request, 'all_adjectives.html', context)