from rest_framework import serializers

from .models import SampleModel

class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SampleModel
        fields = ('title', 'description')