
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from jpskit.views import(
    index,
    kontraktordash,
    kontraktorlist,
    kontraktordaftar
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('kontraktor/dashboard', kontraktordash, name='kontraktor/dashboard'),
    path('kontraktor/senarai', kontraktorlist, name="kontraktor/senarai"),
    path('kontraktor/daftar-baru', kontraktordaftar, name="kontraktor/daftar-baru"),

    #registerpath
    path('kontraktor-add', kontraktordaftar, name="kontraktor-add"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
