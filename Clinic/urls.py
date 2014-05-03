from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	# Direct links from home page
    url(r'^$', TemplateView.as_view(template_name="app/index.html")),
    url(r'^index/$', TemplateView.as_view(template_name="app/index.html")),
	url(r'^appointments/$', TemplateView.as_view(template_name="app/appointments.html")),
	url(r'^faq/$', TemplateView.as_view(template_name="app/faq.html")),
	url(r'^contact/$', TemplateView.as_view(template_name="app/contact.html")),
    url(r'^admin/', include(admin.site.urls)),

    #apps
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^services/', include('services.urls', namespace="services")),
    url(r'^patients/', include('patients.urls', namespace="patients")),
    url(r'^updates/', include('updates.urls', namespace="updates")),    
)
