from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from about import views

urlpatterns = patterns('',
    url(r'^new/$', TemplateView.as_view(template_name="app/new_patients.html")),
    url(r'^testimonials/$', TemplateView.as_view(template_name="app/testimonials.html")),
    url(r'^login/$', TemplateView.as_view(template_name="app/login.html")),
    url(r'^events/$', TemplateView.as_view(template_name="app/about_events.html")),
)