from .models import Recipe
from .serializers import RecipeSerializer

from rest_framework import viewsets

#class RecipeView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Recipe.objects.all()
#    serializer_class = RecipeSerializer
#
#    @classmethod
#    def get_extra_actions(cls):
#        return []

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
