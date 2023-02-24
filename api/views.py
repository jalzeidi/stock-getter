from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import SampleSerializer
from .models import SampleModel

class SampleViewSet(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleSerializer

class FakeView(APIView):
    def get(self, request):
        return Response({'name': 'Neyla'})