from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'Accounts-api-v1'
urlpatterns = [
    path('login', obtain_auth_token),
    path('signup', views.sign_up, name='signup'),
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
