from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class PeopleAPIList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PeopleAPIUpdate(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PeopleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAdminOrReadOnly, )

# class PeopleViewSet(viewsets.ModelViewSet):
#    # queryset = People.objects.all()
#    serializer_class = PeopleSerializer
#
#    def get_queryset(self):
#        pk = self.kwargs.get('pk')
#
#        if not pk:
#            return People.objects.all()[:3]
#
#        return People.objects.filter(pk=pk)
#
#    @action(methods=['get'], detail=True)
#    def category(self, request, pk):
#        cats = Category.objects.get(pk=pk)
#        return Response({'cats': cats.name})
