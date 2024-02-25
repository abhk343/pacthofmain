from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from calendar import month_name
from collections import defaultdict
from django.db.models import Count
from .forms import *



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
            em = Employee.objects.get(Name = e)
            attendance = Attendance(Employee=em,Date=date)
            attendance.save()
        return HttpResponse('form submitted sucesfully')
    return render(request,'home/attendance.html',emp)



def search_absent_employees(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            absences = Attendance.objects.filter(Date__year=year, Date__month=month)
            absent_employee_data = {}
            for absence in absences:
                employee_name = absence.Employee.Name
                absent_date = absence.Date.strftime('%Y-%m-%d')
                if employee_name not in absent_employee_data:
                    absent_employee_data[employee_name] = [absent_date]
                else:
                    absent_employee_data[employee_name].append(absent_date)
            return render(request, 'home/absent_employee.html', {
                'month': month,
                'year': year,
                'absent_employee_data': absent_employee_data,
                'form': form
            })
    else:
        form = SearchForm()
    return render(request, 'home/search_absent.html', {'form': form})