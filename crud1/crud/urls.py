from django.contrib import admin
from django.urls import path
from capp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.home),
    path('user/', views.user),
]
