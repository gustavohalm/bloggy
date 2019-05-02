from rest_framework import serializers
from blog import  models

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        pass

class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model =  models.Post
        fields = [ 'id' , 'author', 'title', 'content']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'author', 'post', 'content']