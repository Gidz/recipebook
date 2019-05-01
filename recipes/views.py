from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import views


class RecipesByUser(views.APIView):
     def get(self, request, format=None, **kwargs):

        username = self.kwargs['user']

        recipe_objects = Recipe.objects.filter(user__username=username)

        recipes = [ recipe.name for recipe in recipe_objects]
        serializer = RecipeSerializer(recipes, many=True)
        return Response(recipes)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
