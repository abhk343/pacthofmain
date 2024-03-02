from django.urls import path,include
from . import views
urlpatterns = [
    #path('hello/',views.hello,name='hello'),
    path('employee/',views.Employees,name='employee'),
   # path('course/<int:course_id>/',views.course_details),
    path('employee_form/',views.EmployeeCreateView,name='employee_form'),
    path('att',views.AddAttendance,name='att'),
    path('search',views.search_absent_employees,name='search'),

]