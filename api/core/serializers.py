from rest_framework import serializers

from api.models import (Album, Company, Track)

#list track
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','track_name']

"""
                            #list the albums and tracks

                            class AlbumToTrackSerializer(serializers.ModelSerializer):
                                    tracks = serializers.SerializerMethodField()
                                    class Meta:
                                        model = Album
                                        fields = '__all__'
                                    
                                    def get_tracks(self, obj):
                                        qs = obj.tracks.all()#.order_by('index')
                                        return TrackSerializer(qs, many=True, read_only=True).data

                            #list company and albums

                            class CompanyToAlbumSerializer(serializers.ModelSerializer):
                                    albums = serializers.SerializerMethodField()
                                    class Meta:
                                        model = Company
                                        fields = '__all__'

                                    def get_albums(self, obj):
                                        qs = obj.albums.all().order_by('index')
                                        return AlbumSerializer(qs, many=True, read_only=True).data
    """

#list albums
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','album_name','stars']

#list Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','company_name']

#list album and company with CU
class AlbumFromCompanySerializerCreateUpdate(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)
    class Meta:
        model = Company
        fields = ['id','company_name','albums']
    def create(self, validated_data):
        albums = validated_data.pop('albums')
        company = Company.objects.create(**validated_data)

        for album in albums:
            Album.objects.create(company=company, **album)
        return company
    
    def update(self, instance, validated_data):
        albums_data = validated_data.pop('albums')
        album_instance = (instance.albums).all()
        album_instance = list(album_instance)

        instance.company_name = validated_data.get('company_name',instance.company_name)
        instance.save()

        for album_data in albums_data:
            album = album_instance.pop(0)
            album.album_name = album_data.get('album_name',album.album_name)
            album.stars = album_data.get('stars',album.stars)
            album.save()
        
        return instance

#list track and album with CU
class TrackFromAlbumSerializerCreateUpdate(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id','album_name','stars','tracks']

    def create(self, validated_data):
        tracks = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)

        for track in tracks:
            Track.objects.create(album=album, **track)
        return album

    def update(self, instance, validated_data):
        tracks_data = validated_data.pop('tracks')
        track_instance = (instance.tracks).all()
        track_instance = list(track_instance)

        instance.album_name = validated_data.get('album_name',instance.album_name)
        instance.stars = validated_data.get('stars', instance.stars)

        for track_data in tracks_data:
            track = track_instance.pop(0)
            track.track_name = track_data.get('track_name',track.track_name)
            track.save()
        return instance