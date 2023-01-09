from django.contrib import admin
from django.urls import path
from application_processing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.initial_view, name='Initial View')
]
