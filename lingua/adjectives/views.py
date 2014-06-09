from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from adjectives.models import Adjective

# Create your views here.
def all_adjectives(request):
	adjectives_list = Adjective.objects.all()
	context = {'adjectives_list': adjectives_list}
	return render(request, 'all_adjectives.html', context)