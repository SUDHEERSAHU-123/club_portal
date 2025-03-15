from django.urls import path
from . import views

urlpatterns = [
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),
    path('events/', views.view_events, name='view_events'),  # Ensure 'view_events' points to your events/home pag
    path('create_event/', views.create_event, name='create_event'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('', views.view_events, name='attendance_home'),  # Default route for /attendance/
    path('mark_attendance/<int:event_id>/', views.mark_attendance, name='mark_attendance'),
    path('view_attendance/<int:event_id>/', views.view_attendance, name='view_attendance'),
]
