from django.conf.urls import patterns, url

from miscellaneous import views

urlpatterns = patterns('',
	url(r'^$', views.all_miscs, name='all_miscs'),
)