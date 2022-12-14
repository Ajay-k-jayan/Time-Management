from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.views import APIView
# import seriliazer and models
from .serializers import UserSerializer
from .models import User
# Create your views here.
from rest_framework.response import Response

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


# Create your views here.

# authetication
# @api_view(['POST'])
# def loginUser(request):
#     if request.method == 'POST':
#         user_data = JSONParser().parse(request)
#         user_serializer = UserSerializer(data=user_data)
#         data = {}
#         if user_serializer.is_valid():
#             user = user_serializer.validated_data['User']
#             try:
#                 UserId = User.objects.get(
#                     UserName=user['UserName'])
#                 if not UserId.check_password(user['Password']):
#                     raise Exception
#                 token = Token.objects.get(user=UserId)
#                 data['token'] = token.key
#                 data['response'] = 'Successful login'
#                 return JsonResponse(data, status=status.HTTP_202_ACCEPTED)
#             except:
#                 data['response'] = "Username or password does not exist"
#                 return JsonResponse(data, status=status.HTTP_401_UNAUTHORIZED)



# user views


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    # get all
    if request.method=='GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    # post
    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            # return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
        # return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Task.objects.all().delete()
        return JsonResponse({'message': '{} Task were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
# get by id
def user_detail(request, pk):
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The id does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data)
     
    
