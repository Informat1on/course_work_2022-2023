from django.contrib import admin
from django.urls import path
from application_processing import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.initial_view, name='Initial View'),
    path('applications/', views.applications_view, name='Applications View'),
    path('workers/', views.workers_view, name='Workers View'),
    path('clients/', views.clients_view, name='Clients View'),
    path('equipment/', views.equipment_view, name='Equipment View'),
    path('reports/', views.reports_view, name='Reports View'),
    path('save_application', views.save_application, name='save_application'),
    path('api/add_position', views.add_position, name='add_position'),
    path('api/add_role', views.add_role, name='add_role'),
    path('api/add_priority', views.add_priority, name='add_priority'),
    path('api/add_status', views.add_status, name='add_status'),
    path('api/add_service_object', views.add_service_object, name='add_service_object'),
    path('api/add_equipment_type', views.add_equipment_type, name='add_equipment_type'),
    path('api/add_equipment', views.add_equipment, name='add_equipment'),
    path('api/delete_equipment', views.delete_equipment, name='delete_equipment'),
    path('api/add_worker', views.add_worker, name='add_worker'),
    path('api/delete_worker', views.delete_worker, name='delete_worker'),
    path('api/add_client', views.add_client, name='add_client'),
    path('api/delete_client', views.delete_client, name='delete_client'),
    path('api/add_application', views.add_application, name='add_application'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
