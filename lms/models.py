from django.db import models
from django.utils import timezone


class Curator(models.Model):
    first_name = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)

class Direction(models.Model):
    name = models.CharField(max_length=20)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE, related_name='direction')

class Disziplina(models.Model):
    name = models.CharField(max_length=20)
    Direction = models.ForeignKey(Disziplina, on_delete=models.CASCADE, related_name='disziplina')

class Group(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='group')

class Student(models.Model):
    name = name = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='student')