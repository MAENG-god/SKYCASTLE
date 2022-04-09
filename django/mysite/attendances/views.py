from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    attendee = []
    attendances = Attendance.objects.all()
    for attendance in attendances:
        attendee.append(attendance.name)
    return render(request, "attendances/index.html", context={"attendees": attendee})
