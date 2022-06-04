from django.urls import path
from user_management import views
from django.contrib.auth import logout

app_name = 'user'

urlpatterns = [
    path('author/signup', views.author_signup, name='author_signup'),
    path('reader/signup', views.reader_signup, name='reader_signup'),
    path('logout', logout, name='logout'),
]
