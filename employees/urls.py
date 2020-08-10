from django.urls import path
from employees.views import PositionList, EmployeeList, EmployeeDetail

urlpatterns = [
    path('position/',PositionList.as_view()),
    path('employees/', EmployeeList.as_view(), name='employees-list'),
    path('employees/<int:pk>', EmployeeDetail.as_view(), name='employees-detail'),

]