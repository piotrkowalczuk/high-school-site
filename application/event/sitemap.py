from django.contrib.sitemaps import Sitemap
from event.models import Event


class EventSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Event.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at