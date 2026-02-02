"""Test urls for the zinnia project"""
from django.contrib import admin
from django.urls import include, path, re_path

from django_xmlrpc.views import handle_xmlrpc

from zinnia.views.channels import EntryChannel

admin.autodiscover()

urlpatterns = [
    re_path(r'^', include('zinnia.urls')),
    path('channel-test/', EntryChannel.as_view(query='test')),
    path('comments/', include('django_comments.urls')),
    path('xmlrpc/', handle_xmlrpc),
    path('admin/', admin.site.urls),
]
