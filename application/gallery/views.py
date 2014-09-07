from common.views import BaseView
from django.shortcuts import render
from gallery.models import Gallery, Photo
from gallery.forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class GalleryIndex(BaseView):
    def get(self, request):

        galleries = Gallery.objects.get_published_for_active_semester()

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

class GalleryArchive(BaseView):
    def get(self, request):
        form = SearchForm(request.GET)
        semester_id = request.GET.get('semester', None)

        galleries = Gallery.objects.get_archived_by_semester(semester_id=semester_id)

        return render(
            request,
            'gallery/archive.html',
            {
                'galleries': galleries,
                'menu': self.get_menu(),
                'form': form,
                'semester_id': semester_id
            }
        )
