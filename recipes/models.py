from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

#TODO: Add relation to Recipe model later
class Step(models.Model):
    step_text = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.step_text[0:10]+".."

#TODO: Add User field, Step field later
class Recipe(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
