from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'sample', SampleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fake', FakeView.as_view()),
]