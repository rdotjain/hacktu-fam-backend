import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Transaction, Piggy_Bank
from .serializers import TransactionSerializer, Piggy_BankSerializer

class MakeTransaction(APIView):
    def post(self, request):
        from_id = request.data['from_id']
        to_id = request.data['to_id']
        amount = request.data['amount']
        saving = request.data['saving']

        t = Transaction(from_id=from_id, to_id=to_id, amount=amount)
        t.save()

        if saving:
            p = Piggy_Bank(student=from_id, amount=amount)
            p.save()
            pass


        from_id.level += 0.2
        points = random.randint(0, 1000)
        from_id.points_earned += points
        to_id.points_earned += points

        from_id.save()
        to_id.save()

        return Response({'message': 'Transaction successful, points earned: ' + str(points), 'status': status.HTTP_200_OK})
    


class GetTransactions(APIView):
    def get(self, request):
        user = request.user
        transactions = Transaction.objects.filter(from_id=user)
        transactions = TransactionSerializer(transactions, many=True)

        return Response({'transactions': transactions})


class GetPiggyBankDeposits(APIView):
    def get(self, request):
        user = request.user
        piggy_bank = Piggy_Bank.objects.filter(student=user)
        piggy_bank = Piggy_BankSerializer(piggy_bank, many=True)

        return Response({'piggy_bank': piggy_bank})


class WithdrawPiggyBank(APIView):
    def post(self, request):
        user = request.user
        amount = request.data['amount']

        piggy_bank = Piggy_Bank.objects.filter(student=user)
        piggy_bank = Piggy_BankSerializer(piggy_bank, many=True)

        total = 0
        for p in piggy_bank:
            total += p.amount

        if total < amount:
            return Response({'message': 'Not enough money in piggy bank'}, status=status.HTTP_400_BAD_REQUEST)

        for p in piggy_bank:
            if p.amount < amount:
                amount -= p.amount
                p.amount = 0
            else:
                p.amount -= amount
                amount = 0
            p.save()

        return Response({'message': 'Withdraw successful'}, status=status.HTTP_200_OK)


class GetPiggyBankBalance(APIView):
    def get(self, request):
        user = request.user
        piggy_bank = Piggy_Bank.objects.filter(student=user)
        piggy_bank = Piggy_BankSerializer(piggy_bank, many=True)

        total = 0
        for p in piggy_bank:
            total += p.amount

        return Response({'balance': total}, status=status.HTTP_200_OK)