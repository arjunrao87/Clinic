from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from about import views

urlpatterns = patterns('',
    url(r'^clinic/$', TemplateView.as_view(template_name="app/about_clinic.html")),
    url(r'^team/$', TemplateView.as_view(template_name="app/about_team.html")),
    url(r'^press/$', TemplateView.as_view(template_name="app/press.html")),
    url(r'^events/$', TemplateView.as_view(template_name="app/events.html")),
)