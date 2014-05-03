from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from about import views

urlpatterns = patterns('',
    url(r'^announcements/$', TemplateView.as_view(template_name="app/announcements.html")),
    url(r'^blog/$', TemplateView.as_view(template_name="app/blog_home.html")),
)