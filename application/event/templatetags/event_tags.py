# -*- coding: utf8 -*-
from calendar import LocaleHTMLCalendar
from django import template
from django.conf import settings
from collections import defaultdict
from datetime import datetime, timedelta, date
from django.template.defaultfilters import date as _date
from django.core.urlresolvers import reverse
from django.utils import timezone

register = template.Library()


@register.tag
def event_calendar(parser, token):
    try:
        tag_name, events = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]

    return EventCalendarNode(events)

class EventCalendarNode(template.Node):
    """
    Process a particular node in the template. Fail silently.
    """

    def __init__(self, events):
        self.events = template.Variable(events)

    def render(self, context):
        try:
            # Get the variables from the context so the method is thread-safe.
            events = self.events.resolve(context)
            cal = EventCalendar(events)
            now = timezone.localtime(timezone.now())

            return cal.formatmonth(now.year, now.month)
        except ValueError as ve:
            print(ve)
            return
        except template.VariableDoesNotExist:
            return


class EventCalendar(LocaleHTMLCalendar):
    """
    Overload Python's calendar.LocaleHTMLCalendar to add the appropriate reading events to
    each day's table cell.
    """

    def __init__(self, events):
        super(EventCalendar, self).__init__(locale=settings.LOCALE_NAME)
        self.events = self.group_by_day(events)

        self.year = 0
        self.month = 0

    def formatday(self, day, weekday):
        cssclass = ''

        if day == 0:
            return self.day_cell('noday', '&nbsp;')

        today = timezone.localtime(timezone.now())
        events = self.events[date(self.year, self.month, day)]

        if len(events):
            cssclass += ' filled'
            body = ['']
            # body = ['<ul></ul>']
            #
            # for event in events:
            #     body.append('<li>')
            #     body.append('<a href="%s">' % event.get_absolute_url())
            #     body.append(event.title)
            #     body.append('</a></li>')
            #
            # body.append('</ul>')

            if today.day == day and today.month == self.month and today.year == self.year:
                return self.day_cell(cssclass, '<span class="today badge">%d</span> %s' % (day, ''.join(body)))
            else:
                return self.day_cell(cssclass, '<span>%d</span> %s' % (day, ''.join(body)))

        if today.day == day:
            return self.day_cell(cssclass, '<span class="today badge">%d</span>' % (day))
        else:
            return self.day_cell(cssclass, '<span>%d</span>' % (day))

    def formatmonth(self, year, month):
        self.year = year
        self.month = month

        v = []
        a = v.append
        a('<div class="panel panel-default">')
        a(self.formatmonthname(year, month, False))
        a('<table class="table table-bordered">')
        a('<thead>')
        a(self.formatweekheader())
        a('</thead>')
        for week in self.monthdays2calendar(year, month):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('<div class="panel-footer text-right">')
        a('<a href="%s" class="small">Wszystkie <i class="glyphicon glyphicon-circle-arrow-right"></i></a>' % reverse('event_list'))
        a('</div>')
        a('</div>')
        a('\n')
        return ''.join(v).encode("utf-8")

    def formatmonthname(self, theyear, themonth, withyear=True):
            return '<div class="panel-heading"><strong>Wydarzenia</strong><span class="pull-right">%s</span></div>' % _date(datetime.now(), "F o")

    def day_cell(self, cssclass, body):
        return '<td class="event-calendar-day %s">%s</td>' % (cssclass, body)

    def group_by_day(self, events):
        d = defaultdict(list)

        for event in events:
            diff = event.end_at - event.start_at
            for i in range(diff.days):
                d[event.start_at.date()+timedelta(days=i)].append(event)

        return d
