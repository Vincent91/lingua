from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from verbs.models import Verb, VerbForm

# Create your views here.
def all_verbs(request):
	if request.method == 'POST':
		form = VerbForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = VerbForm()
	verbs_list = Verb.objects.all()
	context = {'verbs_list': verbs_list, 'form': form}
	return render(request, 'all_verbs.html', context)