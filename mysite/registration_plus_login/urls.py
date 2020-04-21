from django.urls import path
from .views import *
app_name = 'registration'

urlpatterns = [
    path('registration/',registration,name='registration'),
    path('c_registration/',c_registration,name='c_registration'),
    path('request_login/,',request_login,name='request_login'),
    path('log_in/',user_login,name='login'),
    path('log_out/',user_logout,name='logout')
    
]