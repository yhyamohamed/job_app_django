
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.api.v1.urls')),
    path('api/job/', include('job.api.v1.urls')),
    # path('api/', include('django.contrib.auth.urls')),
]
