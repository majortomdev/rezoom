from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UrlobjectViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'urlobjects',UrlobjectViewSet)

urlpatterns = [
    path('',include(router.urls))
]
