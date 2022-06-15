from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Register your models here.
from .models import User, Tag


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'address', 'user_type', 'is_active', 'date_joined', 'all_tags']
    search_fields = ['username', 'tags__name']

    def get_fields(self, request, obj=None):
        fields = super(UserAdmin, self).get_fields(request, obj)
        print(fields)
        if obj:
            fields_to_remove = []
            if request.user.is_superuser:
                fields_to_remove = ["is_staff",
                                    "is_superuser",
                                    "groups",
                                    "user_permissions", "date_of_birth", 'allow_mail_notification', 'date_joined', ]
            for field in fields_to_remove:
                fields.remove(field)
        return fields

    def all_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]


# admin.site.register(User)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
