from rest_framework import serializers
from .models import Drums


class DrumsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'purchaser', 'product', 'description', 'created_at', 'updated_at')
        model = Drums
