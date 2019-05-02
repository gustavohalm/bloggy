from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from blog import models
from . import  serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import filters  

@csrf_exempt
def posts_view(request):
    if request.method == "GET":
        posts = models.Post.objects.all()
        posts_serializer = serializers.PostsSerializers(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)

class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostsSerializers

class CommentViewSet(ModelViewSet):
    
    serializer_class = serializers.CommentsSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(post=self.request.GET['p'])
    