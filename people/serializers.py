import io

from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class PeopleModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class PeopleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = PeopleModel('Angelina Jolie', 'Content: Angelina Jolie')
    model_sr = PeopleSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
    data = JSONParser().parse(stream)
    serializer = PeopleSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
