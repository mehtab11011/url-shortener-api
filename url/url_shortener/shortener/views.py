from django.shortcuts import render
from .models import ShortendURLModel
from .serializers import ShortendURLSerializer
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render

class ShortenURLView(generics.CreateAPIView):
    queryset=ShortendURLModel.objects.all()
    serializer_class=ShortendURLSerializer
    
class ReturnDataView(APIView):
    def get(self, request, Short_URL):
        get_data = get_object_or_404(ShortendURLModel, Short_URL=Short_URL)
        get_data.Access_Count += 1
        get_data.save()
        print(f"Redirecting to: {get_data.Original_URL}")
        return redirect(get_data.Original_URL)

        
class UpdateURLView(generics.UpdateAPIView):
    queryset=ShortendURLModel.objects.all()  
    serializer_class=ShortendURLSerializer  
    lookup_field='Short_URL'

        
class DeleteURLView(generics.DestroyAPIView):
    queryset=ShortendURLModel.objects.all()
    lookup_field="Short_URL"       
    
class CountURlView(APIView):
    def get(selef,request,Short_URL):
        data_get=get_object_or_404(ShortendURLModel,Short_URL=Short_URL)
        data={
            "original_url":data_get.Original_URL,
            "short_url":data_get.Short_URL,
            "count_url":data_get.Access_Count,
            "created_at":data_get.Created_At
        }
        return Response(data,status=status.HTTP_200_OK)
    
    
    
