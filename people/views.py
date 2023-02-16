from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

# class PeopleAPIList(generics.ListCreateAPIView):
#    queryset = People.objects.all()
#   serializer_class = PeopleSerializer


# class PeopleAPIUpdate(generics.UpdateAPIView):
#    queryset = People.objects.all()
#    serializer_class = PeopleSerializer


# class PeopleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = People.objects.all()
#    serializer_class = PeopleSerializer
