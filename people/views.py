from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict


# class PeopleAPIview(generics.ListAPIView):
#    queryset = People.objects.all()
#    serializer_class = PeopleSerializer

class PeopleAPIview(APIView):
    def get(self, request):
        lst = People.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = People.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new)})
