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
        w = People.objects.all()
        return Response({'posts': PeopleSerializer(w, many=True).data})

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method Put not allowed'})

        try:
            instance = People.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = PeopleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})