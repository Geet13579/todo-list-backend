from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


from rest_framework import viewsets
from .serializers import GeeksSerializer, UserRegistrationSerializer,UserLoginSerializer,AddTodoListSerializer
from .models import GeeksModel, UserModel,TodoTaskModel

class GeeksViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer

class UserRegistrationView(APIView):
     def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the password before saving
            user = User(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email']
            )
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
# class LoginAPIView(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = UserLoginSerializer(data=data)
            
#             if serializer.is_valid():
#                 username = serializer.data['username']
#                 password = serializer.data['password']
                
#                 user = authenticate(username=username, password=password)
                
#                 if user is None:
#                     return Response({
#                         'status': 400,
#                         'message': "Invalid password",
#                         'data': {}
#                     })

#                 refresh = RefreshToken.for_user(user)

#                 return Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token)
#                 })
#             else:
#                 return Response({
#                     'status': 400,
#                     'message': "Invalid input data",
#                     'data': serializer.errors
#                 })
#         except Exception as e:
#             return Response({
#                 'status': 500,
#                 'message': "Internal Server Error",
#                 'data': str(e)
#             })
        
class LoginAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            print(data)
            serializer = UserLoginSerializer(data=data)
            
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                
                user = authenticate(username=username, password=password)
                
                if user is None:
                    return Response({
                        'status': 400,
                        'message': "Invalid password",
                        'data': {}
                    })

                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}) 

               
            else:
                return Response({
                    'status': 400,
                    'message': "Invalid input data",
                    'data': serializer.errors
                })
        except Exception as e:
            return Response({
                'status': 500,
                'message': "Internal Server Error",
                'data': str(e)
            })
        

class UserProfileView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
            # Add any other user details you want to include
        }
        return Response(user_data)
    

class TodoListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = AddTodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Set the user to the currently authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request):
        user_tasks = TodoTaskModel.objects.filter(user=request.user)
        serializer = AddTodoListSerializer(user_tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        try:
            # Assuming pk is the auto-generated id field
            todo_list = TodoTaskModel.objects.get(id=pk, user=request.user)
        except TodoTaskModel.DoesNotExist:
            print(f"Todo list with id={pk} and user={request.user} not found.")
            return Response({"error": "Todo list not found"}, status=status.HTTP_404_NOT_FOUND)

        print(f"Deleting todo list: {todo_list}")

        # Delete the todo list object
        todo_list.delete()

        return Response({"message": "Todo list deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        try:
            # Assuming pk is the auto-generated id field
            todo_list = TodoTaskModel.objects.get(id=pk, user=request.user)
        except TodoTaskModel.DoesNotExist:
            print(f"Todo list with id={pk} and user={request.user} not found.")
            return Response({"error": "Todo list not found"}, status=status.HTTP_404_NOT_FOUND)

        print(f"Found todo list: {todo_list}")

        # Update the todo list object with the new data
        serializer = AddTodoListSerializer(todo_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TodoDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
            try:
                todo_list = TodoTaskModel.objects.get(id=pk, user=request.user.id)
                serializer = AddTodoListSerializer(todo_list)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except TodoTaskModel.DoesNotExist:
                return Response({"error": "Todo list not found"}, status=status.HTTP_404_NOT_FOUND)