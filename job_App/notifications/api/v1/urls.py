from django.urls import path
from .views import notification_list

app_name = 'Notifications-api-v1'
urlpatterns = [
    path('notification/<int:id>', notification_list)
]
