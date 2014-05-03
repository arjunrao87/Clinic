from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from about import views

urlpatterns = patterns('',
    url(r'^periodontics/$', TemplateView.as_view(template_name="app/periodontics.html")),
    url(r'^dentistry/$', TemplateView.as_view(template_name="app/dentistry.html")),
)