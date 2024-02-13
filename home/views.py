from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from django.views.generic.edit import CreateView
from django.urls import reverse
# Create your views here.

def hello(request):
    return HttpResponse('hi')

def Employees(request):
    
    employee_list = Employee.objects.all()

    context = {
        'employee_list':employee_list
    }
    return render(request,'home/employees.html',context)


class EmployeeCreateView(CreateView):
    model = Employee
    
    fields = "__all__"

    def get_success_url(self):
       return reverse('employee_form')

def AddAttendance(request):
    emp = {
        'emp':Employee.objects.all()
    }
    if request.method == 'POST':
        employee = request.POST.getlist('Employee')
        date =   request.POST.get('Date')
        for e in employee:
            attendance = Attendance(Employee=e,Date=date)
            attendance.save()
        return HttpResponse("hhjhj")

    return render(request,'home/attendance.html',emp)