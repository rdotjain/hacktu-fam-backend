from rest_framework import serializers

from .models import Student, Merchant, Institute

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('uuid', 'name', 'email', 'institute', 'age', 'level', 'points_earned')


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('uuid', 'name', 'level', 'points_earned')