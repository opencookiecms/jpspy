
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from jpskit.views import(
    index,
)

from jpskit.viewcontroller import (
    perolehanviews,
    kontraktorviews,
    projekview,
    documentviews

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('kontraktor', kontraktorviews.kontraktordash, name='kontraktor'),
    path('kontraktor/senarai', kontraktorviews.kontraktorlist, name="kontraktor/senarai"),
    path('kontraktor/daftar-baru', kontraktorviews.kontraktordaftar, name="kontraktor/daftar-baru"),
    path('kontraktor/edit/<int:id>/',kontraktorviews.kontraktoredit, name="kontraktor/edit"),
    path('kontraktor-delete/<int:id>',kontraktorviews.kontraktordelete, name="kontraktor-delete"),
    path('noperolehan', perolehanviews.dnoperolehan, name="noperolehan"),
    path('noperolehan/daftar',perolehanviews.daftarnoperolehan, name="noperolehan/daftar"),
    path('projek/daftar',projekview.daftarprojek, name="projek/daftar"),
    path('projek/senarai',projekview.senaraiprojek, name="projek/senarai"),
    path('dokumen/mrksatu/daftar/<int:idperolehan>', documentviews.mrkoneregister, name="dokumen/mrksatu/daftar")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
