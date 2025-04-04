from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin_login, name='admin_login'),  # Default route for admin login
    path('events/', views.view_events, name='view_events'),  # Events page (ensure proper name)
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),
    path('create_event/', views.create_event, name='create_event'),
    path('mark_attendance/<int:event_id>/', views.mark_attendance, name='mark_attendance'),
    path('view_attendance/<int:event_id>/', views.view_attendance, name='view_attendance'),
]

