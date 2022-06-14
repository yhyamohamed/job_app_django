from django.urls import path
from .views import job_list, job_details, job_create, job_edit, job_delete, accept_developer, apply_job

app_name = 'job-rest-v1'
urlpatterns = [
    path('', job_list, name='list'),
    path('<int:id>', job_details, name='details'),
    path('create', job_create, name='create'),
    path('<int:id>/edit', job_edit, name='edit'),
    path('<int:id>/delete', job_delete, name='delete'),
    path('<int:id>/accept-developer', accept_developer, name='accept_developer'),
    path('<int:id>/apply', apply_job, name='apply_job'),
]