from django.conf.urls import url
from django.conf.urls import include
from shortenersite.views import index
from shortenersite.views import redirect_original
from shortenersite.views import shorten_url


urlpatterns = [
    url(r'^$', index, name='home'),
    #url(r'^(?P<short_id>\w{6})$', redirect_original, name='redirectoriginal'),			#For Exact 6 characters
    url(r'^(?P<short_id>\w{5,15})$', redirect_original, name='redirectoriginal'),		#For Characters between 5 to 15 (5 & 15 are included)
    url(r'^makeshort/$', shorten_url, name='shortenurl'),
]
