from rest_framework import serializers
from Home.models import *
from users.models import *
from users.forms import *


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
     

class MoviesSerializer(serializers.ModelSerializer):
    director = DirectorsSerializer(many=False)
    genre = GenresSerializer(many=True)

    class Meta:
        model = HomePageModel
        fields = '__all__'



class SeriesSerializer(serializers.ModelSerializer):
    director = DirectorsSerializer(many=False)
    genre = GenresSerializer(many=True)

    class Meta:
        model = Serial
        fields = '__all__'



class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        field = '__all__'
    




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        password = {'password': {'write_only': True}}
    
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



