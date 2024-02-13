from django.urls import path,include
from . import views
urlpatterns = [
    #path('hello/',views.hello,name='hello'),
    path('employee/',views.Employees,name='employee'),
   # path('course/<int:course_id>/',views.course_details),
    path('employee_form/',views.EmployeeCreateView.as_view(),name='employee_form'),
    path('att',views.AddAttendance,name='att')
]