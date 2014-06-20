from common.views import BaseView
from django.shortcuts import render
from gallery.models import Gallery, Photo


class GalleryIndex(BaseView):
    def get(self, request):

        galleries = Gallery.objects.get_all_published()

        return render(
            request,
            'gallery/index.html',
            {
                'galleries': galleries,
                'menu': self.get_menu()
            }
        )

class GalleryShow(BaseView):
    def get(self, request, id):

        gallery = Gallery.objects.get_published(id=id)[0]
        photos = Photo.objects.get_published_by_gallery(gallery_id=id)

        return render(
            request,
            'gallery/show.html',
            {
                'gallery': gallery,
                'photos': photos,
                'menu': self.get_menu()
            }
        )
