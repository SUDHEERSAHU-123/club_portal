from django.db import models

DOMAIN_CHOICES = [
    ('Web Development', 'Web Development'),
    ('Competitive Programming', 'Competitive Programming'),
    ('Data Science', 'Data Science'),
]

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    domain = models.CharField(max_length=30, choices=DOMAIN_CHOICES)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # True = Present, False = Absent

    def __str__(self):
        return f"{self.student.name} - {self.event.name}"

