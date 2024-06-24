from rest_framework import serializers
# from models import Departments, Employees
from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departments
        fields = ('DepartmentId', 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')
