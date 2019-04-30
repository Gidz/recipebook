from django.urls import path

from . import views

urlpatterns = [
        path('api/recipe/', views.RecipeList.as_view()),
        path('api/recipe/<int:pk>/',views.RecipeDetail.as_view())
]
