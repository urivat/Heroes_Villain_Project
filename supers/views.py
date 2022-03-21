from django.http import Http404
from rest_framework.views import APIView
from django.http import Http404
import supers_types
from supers_types.models import SuperType
from supers.serializer import SuperSerializer
from .models import Super
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class SupersList(APIView):

    def get(self, request, format=None):        
        queryset = Super.objects.all()
        super_type = request.query_params.get('type')
        
        if super_type:
            queryset = queryset.filter(type__type=super_type)
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)      


    def post(self, request, format=None):
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_404_NOT_FOUND)
                         
     
            
    



class SupersDetails(APIView):

    def get_object(self, pk):
        try:
            return Super.objects.get(pk=pk)
        except Super.DoesNotExist:
            raise Http404

    def get(self,request,pk, format=None):
        
        supers =self.get_object(pk)
        serializer = SuperSerializer(supers)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        supers = self.get_object(pk)
        serializer=SuperSerializer(supers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        super = self.get_object(pk)
        super.delete
        return Response(status=status.HTTP_204_NO_CONTENT)

class SuperTypesList(APIView):
    def get(self,request,format=None):
        types = SuperType.objects.all()
        dictionary_holder ={}
        for type in types:
            supers = Super.objects.all(type_id=type.id)
            serializer = SuperSerializer(supers, many=True)
            dictionary_holder[supers_types.type]= {
                'supers': serializer.data
            }
        return Response(dictionary_holder)