from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer

@api_view(['GET'])
def get_data(request):
    l1 = [1, 2, 3, 4, 5]
    return Response({"data": l1})

@api_view(['POST'])
def create_student(request):
    std = StudentSerializer(data=request.data)
    if std.is_valid():
        std.save()
        return Response(std.data, status=status.HTTP_201_CREATED)
    return Response(std.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_student_detail(request, student_id):
    try:
        student = Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['PUT'])
def update_student(request, student_id):
    std = Student.objects.get(student_id=student_id)
    serializer = StudentSerializer(std, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request, student_id):
    try:
        student = Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student)
    student.delete()
    return Response(serializer.data)




