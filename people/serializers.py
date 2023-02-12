from rest_framework import serializers
from .models import *


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('title', 'cat_id')