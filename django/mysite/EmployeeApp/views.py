# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# # from models import Departments, Employees
# from . import models
# # from serializers import DepartmentSerializer, EmployeeSerializer
# from . import serializers
#
# # Create your views here.
#
# @csrf_exempt
# def departmentApi(request, id=None):   # keeping an optional id to delete a method
#     if request.method=='GET':   # in GET method we will return all the records in JSON format
#         departments = models.Departments.objects.all()
#         departments_serializer = serializers.DepartmentSerializer(departments,many=True)  # making use of serializer class to convert it into json format
#         return JsonResponse(departments_serializer.data, safe=False)
#     elif request.method == 'POST':
#         department_data = JSONParser().parse(request)  # we are parsing the data
#         departments_serializer = serializers.DepartmentSerializer(data=department_data)  # using serializer to convert it into model
#         if departments_serializer.is_valid():    # if model is valid we will save it into data base
#             departments_serializer.save()
#             return JsonResponse("Added successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#     elif request.method == 'PUT':
#         department_data = JSONParser().parse(request)
#         department = models.Departments.objects.get(DepartmenID=department_data['DepartmentId']) # first we are capturing the existing record using department id
#         departments_serializer = serializers.DepartmentSerializer(department, data=department_data) # mapping it with new values using serializer class
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse("Updated successfully", safe=False)
#         return JsonResponse("Failed to update", safe=False)
#     elif request.method == 'DELETE':
#         department = models.Departments.objects.get(DepartmentID=id)
#         department.delete()
#         return JsonResponse("deleted Successfully", safe=False)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from . import models  # Correctly importing models from the current package
from . import serializers  # Correctly importing serializers from the current package

@csrf_exempt
def departmentApi(request, id=None):   # keeping an optional id to delete a method
    if request.method == 'GET':   # in GET method we will return all the records in JSON format
        departments = models.Departments.objects.all()
        departments_serializer = serializers.DepartmentSerializer(departments, many=True)  # making use of serializer class to convert it into json format
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)  # we are parsing the data
        departments_serializer = serializers.DepartmentSerializer(data=department_data)  # using serializer to convert it into model
        if departments_serializer.is_valid():    # if model is valid we will save it into data base
            departments_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = models.Departments.objects.get(DepartmentID=department_data['DepartmentId'])  # first we are capturing the existing record using department id
        departments_serializer = serializers.DepartmentSerializer(department, data=department_data)  # mapping it with new values using serializer class
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE':
        try:
            department = models.Departments.objects.get(DepartmentID=id)  # Fetch the record by ID
            department.delete()  # Delete the record from the database
            return JsonResponse("Deleted successfully", safe=False)  # Return success message
        except models.Departments.DoesNotExist:
            return JsonResponse("Department not found", safe=False)  # Return error message if record not found
