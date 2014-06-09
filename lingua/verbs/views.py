from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from verbs.models import Verb

# Create your views here.
def all_verbs(request):
	verbs_list = Verb.objects.all()
	context = {'verbs_list': verbs_list}
	return render(request, 'all_verbs.html', context)