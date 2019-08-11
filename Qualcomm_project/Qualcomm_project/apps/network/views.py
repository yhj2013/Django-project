from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView

# Create your views here.

# PUT /networks


class NetworkView(APIView):


    # serialzier_class= ''

    def get(self, requests):

        return Response("successful")