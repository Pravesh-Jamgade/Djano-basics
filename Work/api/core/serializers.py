from rest_framework.serializers import ModelSerializer

from api.models import (Album, Company, Track)




class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','album_name','stars']

class CompanySerializer(ModelSerializer):
    albums = AlbumSerializer(many=True)
    class Meta:
        model = Company
        fields = ['id','company_name','albums']

class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','track_name']