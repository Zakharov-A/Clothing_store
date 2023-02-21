
from django.urls import path


# from users.views import login, registration, profile, logout
from users.views import login, UserRegistrationView, profile, logout


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    # path('registration/', registration, name='registration'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
