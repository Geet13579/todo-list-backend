# import serializer from rest_framework
from rest_framework import serializers
# import model from models.py
from .models import GeeksModel
from .models import UserModel
from .models import TodoTaskModel


from django.contrib.auth.models import User


# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = GeeksModel
		fields = ('title', 'description')



class UserRegistrationSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    


class AddTodoListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    class Meta:
        model = TodoTaskModel
        fields = ('task', 'status','user','date','id')


