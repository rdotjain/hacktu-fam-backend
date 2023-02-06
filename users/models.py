import uuid
from django.db import models


class Level(models.Model):
    level_id = models.IntegerField(primary_key=True, default = 0)
    points = models.IntegerField(default = 0)

    def __str__(self):
        return self.name



class Institute(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    age = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.PROTECT)
    points_earned = models.IntegerField(default = 0)

    def __str__(self):
        return self.name


class Merchant(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def __str__(self):
        return self.name