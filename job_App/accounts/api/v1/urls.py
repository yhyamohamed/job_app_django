from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import profiles, show_profile, update_profile, delete_profile, log_user_out,LogUserIn,list_tags

app_name = 'Accounts-api-v1'
urlpatterns = [
    path('login', LogUserIn.as_view()),
    # path('login', LogUserIn.as_view()),
    path('profile-list', profiles, name='profile'),
    path('profiles/<int:id>', show_profile),
    path('signup', views.sign_up, name='signup'),
    path('profiles/edit/<int:id>', update_profile),
    path('profiles/delete/<int:id>', delete_profile),
    path('tags',list_tags),
    path('logout', log_user_out),

    # path('<int:pk>/delete', views.UserDelete.as_view(), name='signup'),
]

#
# {
#     "username": "yaya2",
#     "email": "yaya@iti.com",
#     "password": "yaya1234",
#     "password_confirmation":"yaya1234",
#     "address": "some where st"
#     "user_type": "recruiter"
# }

# {
#     "username": "yaya",
#     "password": "yaya1234"
# }

# {
#     "token": "817f4b9cb9574ae074b67cee4268cbfec1e60a2f"
# }
