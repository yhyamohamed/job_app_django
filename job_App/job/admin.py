from django.contrib import admin
from .models import Job


# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'creation_time', 'modification_time', 'description', 'developer', 'applied_dev', 'all_tags',
                    'created_by', 'status']
    search_fields = ['developer__username', 'created_by__username']
    list_filter = ('name', 'status')
    def all_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def applied_dev(self, obj):
        return [applied_dev.username for applied_dev in obj.applied_developers.all()]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
