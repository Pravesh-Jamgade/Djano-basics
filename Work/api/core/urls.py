from django.conf.urls import url, include

from api.core import views

urlpatterns = [
    url(r'^$', views.test ),
    url(r'^company/$', views.Companylist.as_view(), name='company-list' ),
    url(r'^company/(?P<pk>[0-9a-f-]+)/$', views.CompanyDetail.as_view(), name='company-detail' ),

    url(r'^album/$', views.Companylist.as_view(), name='album-list' ),
    url(r'^track/$', views.Companylist.as_view(), name='track-list' ),


]
