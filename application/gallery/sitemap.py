from django.contrib.sitemaps import Sitemap
from gallery.models import Gallery, Photo

class GallerySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Gallery.objects.filter(is_published=True)


class PhotoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return Photo.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at