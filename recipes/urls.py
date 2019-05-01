from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import RecipeViewSet

router = routers.DefaultRouter()
router.register('recipes',RecipeViewSet)

urlpatterns = [
    path('api/',include(router.urls))
]