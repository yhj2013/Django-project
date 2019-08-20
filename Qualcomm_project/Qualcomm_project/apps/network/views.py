from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
import psycopg2

from .models import NetworkInfo
from .serializers import NetworkSerializer, UpdateNetworkSerializer


# Create your views here.

# GET  /networks
class NetworkView(APIView):

    def get(self, request):
        data = NetworkInfo.objects.all()
        serializers = NetworkSerializer(data, many=True)
        conn = psycopg2.connect(database="fivedash", user="postgres",
                                password="123456", host="127.0.0.1", port="5432")
        for serializer_data in serializers.data:
            cursor = conn.cursor()
            if serializer_data['country_id'] is None:
                country_sql = 'select country from public.country_gsma where id is null'
                cursor.execute(country_sql)
                country = cursor.fetchall()
                serializer_data['country_id'] = country
            else:
                country_sql = 'select country from public.country_gsma where id={}'.format(serializer_data['country_id'])
                cursor.execute(country_sql)
                country = cursor.fetchall()
                serializer_data['country_id'] = country[0][0]

            if serializer_data['operator_id'] is None:
                operator_sql = 'select operator from public.operator_gsma where id is null'
                cursor.execute(operator_sql)
                operator = cursor.fetchall()
                serializer_data['operator_id'] = operator
            else:
                operator_sql = 'select operator from public.operator_gsma where id={}'.format(
                    serializer_data['operator_id'])
                cursor.execute(operator_sql)
                operator = cursor.fetchall()
                serializer_data['operator_id'] = operator[0][0]
            cursor.close()
        conn.close()
        return Response(serializers.data)


class RetrieveNetworkView(GenericAPIView):
    queryset = NetworkInfo.objects.all()
    serializer_class = NetworkSerializer

    def get(self, request, pk):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        conn = psycopg2.connect(database="fivedash", user="postgres",
                                password="123456", host="127.0.0.1", port="5432")
        cursor = conn.cursor()
        dict = serializer.data
        if serializer.data['country_id'] is None:
            country_sql = 'select country from public.country_gsma where id is null'
            cursor.execute(country_sql)
            country = cursor.fetchall()
            dict['country_id'] = country
        else:
            country_sql = 'select country from public.country_gsma where id={}'.format(serializer.data['country_id'])
            cursor.execute(country_sql)
            country = cursor.fetchall()
            dict['country_id'] = country[0][0]
        if serializer.data['operator_id'] is None:
            operator_sql = 'select operator from public.operator_gsma where id is null'
            cursor.execute(operator_sql)
            operator = cursor.fetchall()
            dict['operator_id'] = operator
        else:
            operator_sql = 'select operator from public.operator_gsma where id={}'.format(serializer.data['operator_id'])
            cursor.execute(operator_sql)
            operator = cursor.fetchall()
            dict['operator_id'] = operator[0][0]
        cursor.close()
        conn.close()
        return Response(dict)


class UpdateNetworkView(GenericAPIView):

    queryset = NetworkInfo.objects.all()
    serializer_class = UpdateNetworkSerializer

    def put(self, request, pk):

        instance = self.get_object()
        serializer = UpdateNetworkSerializer(instance, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)



