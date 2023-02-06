import uuid, random
from django.db import models

from users.models import Student, Merchant


class Transaction(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="from_id"
    )
    to_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="to_id")
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Piggy_Bank(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

