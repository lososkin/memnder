from rest_framework import serializers
from .models import Mem
class MemSerializer(serializers.ModelSerializer):
  class Meta():
    model = Mem
    fields = ('img','text','likes','dislikes')