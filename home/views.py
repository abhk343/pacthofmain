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

def EmployeeCreateView(request):
    if request.method == 'POST':
        form = employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
    else:
        form = employeeform()
    
    return render(request ,'home/employee_form.html',{'forms':form})


def AddAttendance(request):
    emp = {
        'emp': Employee.objects.all()
    }
    if request.method == 'POST':
        employees = request.POST.getlist('Employee')
        date = request.POST.get('Date')
        for employee_name in employees:
            employees_with_name = Employee.objects.filter(Name=employee_name)
            for em in employees_with_name:
                attendance = Attendance(Employee=em, Date=date)
                attendance.save()
        return HttpResponse('Form submitted successfully')
    return render(request, 'home/attendance.html', emp)



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
            return render(request, 'home/view_attendance.html', {
                'month': month,
                'year': year,
                'absent_employee_data': absent_employee_data,
                'form': form
            })
    else:
        form = SearchForm()
    return render(request, 'home/search_absent.html', {'form': form})