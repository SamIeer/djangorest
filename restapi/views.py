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

# @api_view(['PUT'])
# def update_student(request , id):
#     try:
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializer(student_obj , data = request.data)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status' : 403 , 'errors' : serializer.errors , 'message':'something went wrong'})
#         serializer.save()
#         return Response({'status' : 200 , 'payload' : serializer.data , 'message' : 'your data sent'})
#     except Exception as e:
#         return Response({'status':403 , 'message':'invalid id'})
    
@api_view(['PATCH'])
def update_student(request , id):

    try:
        student_obj = Student.objects.get(id = id)
        serializer = StudentSerializer(student_obj , data = request.data , partial = True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 , 'errors' : serializer.errors , 'message':'something went wrong'})
        serializer.save()
        return Response({'status' : 200 , 'payload' : serializer.data , 'message' : 'your data sent'})
    
    except Exception as e:
        return Response({'status':403 , 'message':'invalid id'})
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        # id = request.GET.get('id')
        Student_obj = Student.objects.get(id = id)
        Student_obj.delete()
        return Response({'status':200 , 'message': 'deleted'})
    except Exception as e:
        print(e)
        return Response({'status':403 , 'message' : 'invlaid id'}) 