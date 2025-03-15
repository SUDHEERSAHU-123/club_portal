from django.contrib import admin
from .models import Student, Event, Attendance





class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'student', 'status')  # Show these fields in the admin list view
    list_filter = ('event', 'status')             # Add filters for easier searching
    search_fields = ('event__name', 'student__name')  # Add a search bar

admin.site.register(Event)
admin.site.register(Student)
admin.site.register(Attendance, AttendanceAdmin)
