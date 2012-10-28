from django.conf.urls import patterns, url

from instagram_loader import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
    url(r'^instagram/subscription$', views.subscription, name='subscription'), 
)