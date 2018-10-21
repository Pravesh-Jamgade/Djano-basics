from django.contrib import admin


from api.models import(Company, Track, Album)
# Register your models here.
admin.site.register(Company)
admin.site.register(Track)
admin.site.register(Album)
