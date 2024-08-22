from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CreateUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]


class GetUserView(APIView):
    def get(self, request):
        user_name = request.query_params.get('username')
        user_id = request.query_params.get('id')

        if user_name:
            try:
                username = User.objects.get(username=user_name)
                serializer_user = UserSerializer(username)
                return Response(serializer_user.data, status=status.HTTP_200_OK)
            except:
                return Response({'detail' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        elif user_id:
            try:
                userId = User.objects.get(id=user_id)
                serializer_id = UserSerializer(userId)
                return Response(serializer_id.data, status=status.HTTP_200_OK)
            except:
                return Response({'detail' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response({'detail' : 'Add username or id as a query parameter'}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateUserView(APIView):
    def put(self, request):
        user_name = request.query_params.get('username')
        user_id = request.query_params.get('id')
        new_name = request.data.get('username')

        if user_name:
            try:
                username = User.objects.get(username=user_name)
                username.username = new_name
                username.save()
                serializer_name = UserSerializer(username)
                return Response(serializer_name.data, status=status.HTTP_200_OK)
            except:
                return Response({'detail' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        elif user_id:
            try:
                userId = User.objects.get(id=user_id)
                userId.username = new_name
                userId.save()
                serializer_id = UserSerializer(userId)
                return Response(serializer_id.data, status=status.HTTP_200_OK)

            except:
                return Response({"detail" : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response({"detail" : 'Add username or id as a query parameter'}, status=status.HTTP_404_NOT_FOUND)


class DeleteUserView(APIView):
    def delete(self, request):
        user_name = request.query_params.get('username')
        user_id = request.query_params.get('id')

        if user_name:
            try:
                username = User.objects.get(username=user_name)
                username.delete()
                return Response({'success' : 'User was deleted'}, status=status.HTTP_200_OK)
            except:
                return Response({'detail' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        elif user_id:
            try:
                userId = User.objects.get(id=user_id)
                userId.delete()
                return Response({'success' : 'User was deleted'}, status=status.HTTP_200_OK)
            except:
                return Response({'detail' : 'Not Found'})
            
        else:
            return Response({"detail" : 'Add username or id as a query parameter'}, status=status.HTTP_404_NOT_FOUND)
