from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^nouns/', include('nouns.urls', namespace = 'nouns')),
    url(r'^verbs/', include('verbs.urls', namespace = 'verbs')),
    url(r'^adjectives/$', include('adjectives.urls', namespace = 'adjectives')),
    url(r'^miscellaneous/$', include('miscellaneous.urls', namespace = 'miscellaneous')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
