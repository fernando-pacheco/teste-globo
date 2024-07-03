from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramDataViewSet

router = DefaultRouter()
router.register(r'program-data', ProgramDataViewSet, basename='program-data')

urlpatterns = [
    path('', include(router.urls)),
]
