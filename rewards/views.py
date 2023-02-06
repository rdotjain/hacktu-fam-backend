from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Reward, RewardGroupToUserMapping
from .serializers import RewardSerializer, UserRewardSerializer

def calculate_reward_group(user_id, transaction_id):
    pass

class TransactionReward(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        transaction_id = request.data['transaction_id']
        reward_group = calculate_reward_group(user_id, transaction_id)
        reward = Reward.objects.filter(reward_group=reward_group).order_by('?').first()

        r = RewardGroupToUserMapping(user=user_id, reward=reward)
        r.save()

        return Response({'message': 'Reward given'}, status=status.HTTP_200_OK)


class GetRewards(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        rewards = RewardGroupToUserMapping.objects.filter(user=user_id)
        serializer = UserRewardSerializer(rewards, many=True)
        return Response({'rewards': serializer.data}, status=status.HTTP_200_OK)


class RedeemReward(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        reward_id = request.data['reward_id']

        reward = RewardGroupToUserMapping.objects.get(user=user_id, reward=reward_id)
        reward.redeemed = True
        reward.save()

        return Response({'message': 'Reward redeemed'}, status=status.HTTP_200_OK)