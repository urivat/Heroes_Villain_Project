
from rest_framework.views import APIView
from rest_framework import status
from supers_types.models import SuperType
from supers_types.serializer import SuperTypeSerializer
from rest_framework.response import Response
from django.http import Http404
# Create your views here.
class TypeList(APIView):
    

    def get(self, request, format=None):
        type = SuperType.objects.all()
        type_serializer = SuperTypeSerializer(type, many=True)
        return Response(type_serializer.data)

    def post(self, request, format=None):
        serializer = SuperTypeSerializer(request.data)
        if serializer.is_valid(raise_exception=True, status=):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)