from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class PeopleAPIview(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
