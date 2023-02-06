from django.shortcuts import render
from .models import Student, Merchant, Institute

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentsOnboard(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        institute = request.data['institute']
        age = request.data['age']

        s = Student(name=name, email=email, institute=institute, age=age)
        s.save()

        # TODO: Student verification and KYC

        return Response({'message': 'Student onboarded'}, status=status.HTTP_200_OK)


class MerchantsOnboard(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        institute = request.data['institute']

        m = Merchant(name=name, email=email, institute=institute)
        m.save()

        # TODO: Merchant verification and KYC

        return Response({'message': 'Merchant onboarded'}, status=status.HTTP_200_OK)

class Leaderboard(APIView):
    def post(self, request):
        institute = request.data['institute']
        students = Student.objects.filter(institute=institute)
        students = sorted(students, key=lambda x: x.points_earned, reverse=True)
        students = students[:10]
        return Response({'students': students}, status=status.HTTP_200_OK)