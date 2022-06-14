from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'address', 'user_type', 'is_active', 'date_joined', 'all_tags', 'address']
    search_fields = ['username', 'all_tags']

    def get_fields(self, request, obj=None):
        fields = super(UserAdmin, self).get_fields(request, obj)
        print(fields)
        if obj:
            fields_to_remove = []
            if request.user.is_superuser:
                fields_to_remove = ["is_staff",
                                    "is_superuser",
                                    "groups",
                                    "user_permissions","date_of_birth",'allow_mail_notification' ,'date_joined',]
            for field in fields_to_remove:
                fields.remove(field)
        return fields

    def all_tags(self, obj):
        print(all)
        return "\n".join([p.name for p in obj.tags.all()])
# admin.site.register(User)
