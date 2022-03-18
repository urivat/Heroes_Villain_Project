from django.http import Http404
from rest_framework.views import APIView
from supers.serializer import SupersSerializer

from supers_types import serializer
from supers.serializer import SuperSerializer 
from .models import Super
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class SupersList(APIView):

    def get(self, request, format=None):
        super_types = request.query_params.get('supers_types_id')
        sort_param =request.query_params.get('sort')
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_404_NOT_FOUND)




class SupersDetails(APIView):

    def get(self):
        pass


