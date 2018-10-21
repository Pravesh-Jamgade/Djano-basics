from django.conf.urls import url, include

from api.core import views

urlpatterns = [
    url(r'^$', views.test ),
    url(r'^company/$', views.Companylist.as_view(), name='company-list' ),
    url(r'^company/(?P<pk>[0-9a-f-]+)/$', views.CompanyDetail.as_view(), name='company-detail' ),

    url(r'^album/$', views.Albumlist.as_view(), name='album-list' ),
    url(r'^track/$', views.Tracklist.as_view(), name='track-list' ),
    
    url(r'^company/album/$', views.AlbumFromCompany.as_view(), name='albums-from-company' ),
    url(r'^company/album/(?P<pk>[0-9a-f-]+)/$', views.AlbumFromCompanyDetail.as_view(), name='detail-albums-from-company' ),

    url(r'^album/track/$', views.TrackFromAlbum.as_view(), name='tracks-from-album' ),
    url(r'^album/track/(?P<pk>[0-9a-f-]+)/$', views.TrackFromAlbumDetail.as_view(), name='detail-tracks-from-album' ),
    


    #url(r'^company/album/$', views.CompanyToAlbumView.as_view(), name='new-albums-from-company' ),
    #url(r'^company/album/track/$', views.AlbumToTrackView.as_view(), name='new-tracks-from-album' ),
 
    


]
