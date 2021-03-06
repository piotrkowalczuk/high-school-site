# -*- coding: utf-8 -*-
"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'verstyle.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.Group(
            column=1,
            collapsible=False,
            children=[
                modules.ModelList(
                    title='Treść',
                    collapsible=False,
                    models=(
                        'news.models.News', 
                        'page.models.Page', 
                        'links.models.Link',
                        'event.*'
                    )
                ),
                modules.ModelList(
                    title='Zdjęcia',
                    collapsible=False,
                    models=('gallery.models.Gallery', 'gallery.models.Photo')
                ),
                modules.ModelList(
                    title='Ustawienia',
                    collapsible=False,
                    models=('semester.models.Semester', 'category.models.Category')
                ),
                modules.ModelList(
                    title='Użytkownicy',
                    collapsible=False,
                    models=('user.models.User',)
                ),
                # modules.AppList(
                #     title='Wydarzenia',
                #     column=1,
                #     models=('schedule.*',)
                # ),
            ]
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            'Zarządzanie mediami',
            column=3,
            collapsible=False,
            children=[
                {
                    'title': 'Przeglądarka plików',
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            'Ostatnie akcje',
            limit=8,
            collapsible=False,
            column=3,
        ))
