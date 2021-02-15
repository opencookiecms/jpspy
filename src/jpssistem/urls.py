
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
    path('kontraktor/profile/<int:kontrakid>', kontraktorviews.kontraktorprofile, name="kontraktor/profile"),
    path('kontraktor/daftar-baru', kontraktorviews.kontraktordaftar, name="kontraktor/daftar-baru"),
    path('kontraktor/edit/<int:id>/',kontraktorviews.kontraktoredit, name="kontraktor/edit"),
    path('kontraktor-delete/<int:id>',kontraktorviews.kontraktordelete, name="kontraktor-delete"),
    path('noperolehan', perolehanviews.dnoperolehan, name="noperolehan"),
    path('noperolehan/daftar',perolehanviews.daftarnoperolehan, name="noperolehan/daftar"),
    path('projek/daftar',projekview.daftarprojek, name="projek/daftar"),
    path('projek/senarai',projekview.senaraiprojek, name="projek/senarai"),
    path('dokumen/mrksatu/<int:idperolehan>', documentviews.mrkone, name="dokumen/mrksatu"),
    path('dokumen/mrkdua/<int:idperolehan>', documentviews.mrktwo, name="dokumen/mrkdua"),
    path('dokumen/lsk/<int:idperolehan>', documentviews.laporansiapkerja, name="dokumen/lsk"),
    path('dokumen/mrktiga/<int:idperolehan>', documentviews.mrktiga, name="dokumen/mrktiga"),
    path('dokumen/psk/<int:idperolehan>', documentviews.psk, name="dokumen/psk"),
    path('dokumen/senaraisemakan/<int:idperolehan>', documentviews.ssv, name="dokumen/senaraisemakan"),
    path('dokumen/psmk/<int:idperolehan>',documentviews.psmkview, name="dokumen/psmk"),
    path('dokumen/jaminanbank/<int:idperolehan>',documentviews.jaminanbankv, name="dokumen/jaminanbank"),
    path('dokumen/ppwjp/<int:idperolehan>',documentviews.pwjpview, name="dokumen/ppwjp"),
    path('dokumen/smrk/<int:idperolehan>',documentviews.smrkview, name="dokumen/smrk"),
    path('dokumen/skhas/<int:idperolehan>',documentviews.skhasview, name="dokumen/skhas"),
    path('dokumen/suratbon/<int:idperolehan>',documentviews.sbonview, name="dokumen/suratbon"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
