from rest_framework import serializers
from .models import *


# class PeopleModel:
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"

# def encode():
#    model = PeopleModel('Angelina Jolie', 'Content: Angelina Jolie')
#    model_sr = PeopleSerializer(model)
#    json = JSONRenderer().render(model_sr.data)
#    print(json)
#
#
# def decode():
#    stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#    data = JSONParser().parse(stream)
#    serializer = PeopleSerializer(data=data)
#    serializer.is_valid()
#   print(serializer.validated_data)
