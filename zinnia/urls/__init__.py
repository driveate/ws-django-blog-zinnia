"""Defaults urls for the Zinnia project"""
from django.urls import include, path
from django.utils.translation import gettext_lazy

from zinnia.settings import TRANSLATED_URLS


def i18n_url(url, translate=TRANSLATED_URLS):
    """
    Translate or not an URL part.
    """
    return gettext_lazy(url) if translate else url


_ = i18n_url

app_name = 'zinnia'

urlpatterns = [
    path(_('feeds/'), include('zinnia.urls.feeds')),
    path(_('tags/'), include('zinnia.urls.tags')),
    path(_('authors/'), include('zinnia.urls.authors')),
    path(_('categories/'), include('zinnia.urls.categories')),
    path(_('search/'), include('zinnia.urls.search')),
    path(_('random/'), include('zinnia.urls.random')),
    path(_('sitemap/'), include('zinnia.urls.sitemap')),
    path(_('trackback/'), include('zinnia.urls.trackback')),
    path(_('comments/'), include('zinnia.urls.comments')),
    path('', include('zinnia.urls.entries')),
    path('', include('zinnia.urls.archives')),
    path('', include('zinnia.urls.shortlink')),
    path('', include('zinnia.urls.quick_entry')),
    path('', include('zinnia.urls.capabilities')),
]
