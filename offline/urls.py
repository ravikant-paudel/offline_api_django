# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("profiles", views.UserProfileViewSet)

urlpatterns = router.urls