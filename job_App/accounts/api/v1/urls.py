from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import profiles,show


app_name = 'Accounts-api-v1'
urlpatterns = [
    path('login', obtain_auth_token),
    # path('developer-signup', views.signup, name='signup'),
    path('company-signup', views.company_sign_up, name='signup'),
    path('profile-list',profiles, name='profile'),
    path('<int:id>',show),
]

#
# {
#     "username": "yaya",
#     "email": "yaya@iti.com",
#     "password": "yaya1234",
#     "password_confirmation":"yaya1234",
#     "address": "some where st"
# }

# {
#     "username": "yaya",
#     "password": "yaya1234"
# }

# {
#     "token": "817f4b9cb9574ae074b67cee4268cbfec1e60a2f"
# }