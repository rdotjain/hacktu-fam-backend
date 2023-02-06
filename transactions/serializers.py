from rest_framework import serializers

from .models import Transaction, Piggy_Bank

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('from_id', 'to_id', 'amount', 'saving')


class Piggy_BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piggy_Bank
        fields = ('student', 'amount', 'saving', 'timestamp')