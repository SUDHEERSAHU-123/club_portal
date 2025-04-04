from django.shortcuts import render, redirect
from .models import Event, Student, Attendance
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Attendance

from datetime import date
# Function to create an event

def admin_login(request):
    print("Admin Login View is called!")  # Debugging line
    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get() to avoid errors
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:  # Allow only staff/admin users
            login(request, user)
            return redirect('view_events')  # Redirect to the events page
        elif user is not None and not user.is_staff:
            messages.error(request, "You do not have admin privileges.")
        else:
            messages.error(request, "Invalid username or password.")  # Handle invalid credentials
            return render(request, 'attendance/admin_login.html')  # Reload with error
    return render(request, 'attendance/admin_login.html')        

def create_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        description = request.POST['description']

        # Create the event
        event = Event.objects.create(name=name, date=date, description=description)

        # Automatically add all students to the event's attendance
        students = Student.objects.all()  # Adjust query to include only relevant students
        for student in students:
            Attendance.objects.get_or_create(event=event, student=student)

        return redirect('view_events')  # Redirect after event creation
    return render(request, 'attendance/create_event.html')


# Function to view all events
def view_events(request):
    events = Event.objects.all()
    return render(request, 'attendance/view_events.html', {'events': events})



def mark_attendance(request, event_id):
    # Fetch the event by ID
    event = get_object_or_404(Event, id=event_id)
    today = date.today()  # Get today's date

    # Restrict attendance marking to the event date
    if event.date != today:
        return render(request, 'attendance/error.html', {
            'error': f"Attendance for this event can only be taken on {event.date.strftime('%Y-%m-%d')}.",
            'event': event
        })

    # Fetch attendance records for the event
    attendance_records = Attendance.objects.filter(event=event)

    if request.method == 'POST':
        # Update attendance status based on form submission
        for record in attendance_records:
            status = request.POST.get(f'status_{record.student.id}', 'off') == 'on'
            record.status = status
            record.save()
        return redirect('view_events')

    # Pass data to the template
    return render(request, 'attendance/mark_attendance.html', {
        'event': event,
        'attendance_records': attendance_records
    })


# Function to view attendance records
def view_attendance(request, event_id):
    event = Event.objects.get(id=event_id)
    attendance_records = Attendance.objects.filter(event=event)
    return render(request, 'attendance/view_attendance.html', {'event': event, 'attendance_records': attendance_records})




from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Attendance

def edit_attendance(request):
    if request.method == 'POST':
        # Check if the "Search" button was clicked
        if 'search' in request.POST:
            event_name = request.POST.get('event_name')
            event_date = request.POST.get('event_date')

            # Validate inputs
            if not event_name or not event_date:
                return render(request, 'attendance/edit_attendance.html', {
                    'error': 'Event name and date are required to search.'
                })

            try:
                # Fetch the event and its attendance records
                event = Event.objects.get(name=event_name, date=event_date)
                attendance_records = Attendance.objects.filter(event=event)
                return render(request, 'attendance/edit_attendance_form.html', {
                    'event': event,
                    'attendance_records': attendance_records
                })

            except Event.DoesNotExist:
                return render(request, 'attendance/edit_attendance.html', {
                    'error': 'Event not found. Please check the event name and date.'
                })

        # Check if the "Save Changes" button was clicked
        elif 'save_changes' in request.POST:
            # Save attendance changes
            event_id = request.POST.get('event_id')  # Ensure event ID is passed from the form
            event = get_object_or_404(Event, id=event_id)
            attendance_records = Attendance.objects.filter(event=event)

            for record in attendance_records:
                status = request.POST.get(f'status_{record.student.id}', 'off') == 'on'
                record.status = status
                record.save()

            # Redirect to the home page after saving
            return redirect('view_events')  # Ensure 'view_events' matches your URL name for the home page

    # Default GET request renders the search form
    return render(request, 'attendance/edit_attendance.html')

