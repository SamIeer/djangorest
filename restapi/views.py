from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serilizer import StudentSerializer
# Create your views here.
@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs , many=True)

    return Response({'status': 200 , 'payload': serializer.data})

@api_view(['POST'])
def postdata(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status' : 403 ,'errors' : serializer.errors , 'message' : 'something went wrong'})
    serializer.save()
    return Response({'status':200 , 'payload' : serializer.data , 'message' : 'you sent'})