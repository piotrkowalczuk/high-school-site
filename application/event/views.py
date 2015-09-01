from common.views import BaseView
from django.shortcuts import render
from event.forms import FilterForm
from models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class EventList(BaseView):
    def get(self, request):
        form = FilterForm(request.GET)

        semester_id = int('0' + request.GET.get('semester', '0'))
        category_id = int('0' + request.GET.get('category', '0'))
        status = int('0' + request.GET.get('status', '0'))

        published_events = Event.objects.get_filtered(semester_id, category_id, status)
        if status == 0 and category_id == 0 and semester_id == 0 and len(published_events) < 10:
            published_events = Event.objects.get_filtered(semester_id, category_id, 1)

        paginator = Paginator(published_events, 10)

        try:
            events = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        return render(
            request,
            'event/index.html',
            {
                'events': events,
                'menu': self.get_menu(),
                'form': form,
                'semester_id': semester_id,
                'category_id': category_id,
                'status': status,
            }
        )

class EventDetails(BaseView):
    def get(self, request, slug):
        published_event = Event.objects.get_by_slug(slug)

        return render(
            request,
            'event/details.html',
            {
                'event': published_event,
                'menu': self.get_menu()
            }
        )