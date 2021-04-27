
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
    documentviews,
    reportview

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
    path('projek/senarai-dokumen/<int:prid>', projekview.dokumenpilih, name="projek/senarai-dokumen"),
    path('projek/maklumatperolehan', projekview.maklumatperolehan, name="projek/maklumatperolehan"),
    path('projek/maklumatperolehan/<str:jenisp>', projekview.maklumatperolehanjenis, name="projek/maklumatperolehan/"),   
    path('projek/kodvot/<str:kvd>', projekview.projekkodvot, name="projek/kodvot/"),  
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


    path('laporan/pdf/<int:idperolehan>', reportview.some_pdf, name="laporan/pdf"),
    path('laporan/excel/<int:idperolehan>', reportview.some_excel, name="laporan/excel"),
    path('laporan/filter', reportview.report_by_year, name="laporan/filter"),
    path('laporan/excel', reportview.testexcel, name="laporan/excel"),
    path('laporan/mrksatu/<int:idperolehan>', reportview.pdfmrksatu, name="laporan/mrksatu"),
    path('laporan/mrkdua/<int:idperolehan>',reportview.pdfmrkdua, name="laporan/mrkdua"),
    path('laporan/lsk/<int:idperolehan>',reportview.pdflsk, name="laporan/lsk"),
    path('laporan/mrktiga/<int:idperolehan>',reportview.pdfmrktiga, name="laporan/mrktiga"),

    path('sistem/subsistem', projekview.load_sistem, name="sistem/subsistem"),
    path('sistem/komponen', projekview.load_component, name="sistem/komponen"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
