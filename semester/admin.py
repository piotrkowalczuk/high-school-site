from django.contrib import admin
from semester.models import Semester


class SemesterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'start_at',
        'end_at'
    )


admin.site.register(Semester, SemesterAdmin)
