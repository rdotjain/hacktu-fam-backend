import uuid

from django.db import models
from users.models import Student, Level


class Reward(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reward_group = models.ForeignKey(Level, on_delete=models.PROTECT)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RewardGroupToUserMapping(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    redeemed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
