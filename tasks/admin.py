from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    # list_display = ('id', 'title', 'description', 'created', 'datecompleted', 'important', 'user')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', 'description', 'user')
    # list_per_page = 25
# Register your models here.


admin.site.register(Task, TaskAdmin)