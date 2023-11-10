from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts import views

urlpatterns = [
    path('signin', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
]
