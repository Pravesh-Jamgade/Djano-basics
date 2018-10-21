from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from api.models import(Album, Company, Track)
from api.core.serializers import (AlbumSerializer, CompanySerializer,
                                 TrackSerializer, AlbumFromCompanySerializerCreateUpdate,
                                 TrackFromAlbumSerializerCreateUpdate,
                                )
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def test(request):
    return HttpResponse('<h3>Test</h3>')

class Albumlist(APIView):
    def get(self, request):
        object = Album.objects.all()
        serialize = AlbumSerializer(object, many=True)
        return Response(serialize.data)

class Companylist(APIView):
    def get(self, request):
        object = Company.objects.all()
        serialize = CompanySerializer(object, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = CompanySerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetail(APIView):
    def get_object(self, pk):
            try:
                return Company.objects.get(pk=pk)
            except File.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
         object = self.get_object(pk=pk)
         serial = CompanySerializer(object)
         return Response(serial.data)

    def put(self, request, pk, format=None):
        object = self.get_object(pk=pk)
        serialize = CompanySerializer(object, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Tracklist(APIView):
    def get(self, request):
        object = Track.objects.all()
        serialize = TrackSerializer(object, many=True)
        return Response(serialize.data)
      
class AlbumFromCompany(APIView):
    def get(self, request):
        object = Company.objects.all()
        serialize = AlbumFromCompanySerializerCreateUpdate(object, many=True)
        return Response(serialize.data)
    def post(self, request):
        serialize = AlbumFromCompanySerializerCreateUpdate(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumFromCompanyDetail(APIView):
    def get_object(self, pk):
            try:
                return Company.objects.get(pk=pk)
            except File.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
         object = self.get_object(pk=pk)
         serial = AlbumFromCompanySerializerCreateUpdate(object)
         return Response(serial.data)

    def put(self, request, pk, format=None):
        object = self.get_object(pk=pk)
        serialize = AlbumFromCompanySerializerCreateUpdate(object, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TrackFromAlbum(APIView):
    def get(self, request):
        object = Album.objects.all()
        serialize = TrackFromAlbumSerializerCreateUpdate(object, many=True)
        return Response(serialize.data)
    
    def post(self, request):
        serialize = TrackFromAlbumSerializerCreateUpdate(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackFromAlbumDetail(APIView):
    def get_object(self, pk):
            try:
                return Album.objects.get(pk=pk)
            except File.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
         object = self.get_object(pk=pk)
         serial = TrackFromAlbumSerializerCreateUpdate(object)
         return Response(serial.data)

    def put(self, request, pk, format=None):
        object = self.get_object(pk=pk)
        serialize = TrackFromAlbumSerializerCreateUpdate(object, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

"""
                                                class CompanyToAlbumView(APIView):
                                                    def get(self, request):
                                                        object = Company.objects.all()
                                                        serialize = CompanyToAlbumSerializer(object, many=True)
                                                        return Response(serialize.data)
                                                        
                                                class AlbumToTrackView(APIView):
                                                        def get(self, request):
                                                            object = Album.objects.all()
                                                            serialize = AlbumToTrackSerializer(object, many=True)
                                                            return Response(serialize.data)

"""