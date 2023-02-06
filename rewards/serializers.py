from rest_framework import serializers

from .models import Reward, RewardGroupToUserMapping


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('uuid', 'reward_group', 'description')


class UserRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardGroupToUserMapping
        fields = ('uuid', 'user', 'reward', 'redeemed')