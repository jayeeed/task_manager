from django.db.models import Case, When, IntegerField
from django.contrib import admin
from .models import Task, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class TaskAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]
    list_display = ('title', 'due_date', 'priority', 'user', 'is_complete')
    list_filter = ('creation_date', 'due_date', 'priority', 'is_complete')
    search_fields = ('title',)
    ordering = (Case(
        When(priority='High', then=1),
        When(priority='Medium', then=2),
        When(priority='Low', then=3),
        default=4,
        output_field=IntegerField(),
    ),)

admin.site.site_header = 'TM Admin'
admin.site.site_title = 'TM Admin'
admin.site.index_title = 'TM Admin'

admin.site.register(Task, TaskAdmin)
