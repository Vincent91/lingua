from django.http import HttpResponseRedirect
from django.shortcuts import render

from miscellaneous.models import MiscForm, Misc

# Create your views here.
def all_miscs(request):
	if request.method == 'POST':
		form = MiscForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = MiscForm()
	miscs_list = Misc.objects.all()
	context = {'miscs_list': miscs_list, 'form': form}
	return render(request, 'all_miscs.html', context)