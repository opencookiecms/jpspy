
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
import uuid

from jpskit.views import(
    index,
)

from jpskit.viewcontroller import (
    perolehanviews,
    kontraktorviews,
    projekview,
    documentviews,
    reportview,
    authviews,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('kontraktor', kontraktorviews.kontraktordash, name='kontraktor'),
    path('kontraktor/senarai', kontraktorviews.kontraktorlist, name="kontraktor/senarai"),
    path('kontraktor/profile/<uuid:kontrakid>', kontraktorviews.kontraktorprofile, name="kontraktor/profile"),
    path('kontraktor/daftar-baru', kontraktorviews.kontraktordaftar, name="kontraktor/daftar-baru"),
    path('kontraktor/edit/<int:id>/',kontraktorviews.kontraktoredit, name="kontraktor/edit"),
    path('kontraktor-delete/<int:id>',kontraktorviews.kontraktordelete, name="kontraktor-delete"),
    path('noperolehan', perolehanviews.dnoperolehan, name="noperolehan"),
    path('noperolehan/daftar',perolehanviews.daftarnoperolehan, name="noperolehan/daftar"),
    path('projek/daftar',projekview.daftarprojek, name="projek/daftar"),
    path('projek/senarai',projekview.senaraiprojek, name="projek/senarai"),
    path('projek/senarai-dokumen/<uuid:prid>', projekview.dokumenpilih, name="projek/senarai-dokumen"),
    path('projek/maklumatperolehan', projekview.maklumatperolehan, name="projek/maklumatperolehan"),
    path('projek/maklumatperolehan/<str:jenisp>', projekview.maklumatperolehanjenis, name="projek/maklumatperolehan/"),   
    path('projek/kodvot/<int:kvd>', projekview.projekkodvot, name="projek/kodvot/"),  
    path('dokumen/mrksatu/<uuid:projekid>', documentviews.mrkone, name="dokumen/mrksatu"),
    path('dokumen/mrkdua/<uuid:projekid>', documentviews.mrktwo, name="dokumen/mrkdua"),
    path('dokumen/lsk/<uuid:projekid>', documentviews.laporansiapkerja, name="dokumen/lsk"),
    path('dokumen/mrktiga/<uuid:projekid>', documentviews.mrktiga, name="dokumen/mrktiga"),
    path('dokumen/psk/<uuid:projekid>', documentviews.psk, name="dokumen/psk"),
    path('dokumen/senaraisemakan/<uuid:projekid>', documentviews.ssv, name="dokumen/senaraisemakan"),
    path('dokumen/psmk/<uuid:projekid>',documentviews.psmkview, name="dokumen/psmk"),
    path('dokumen/jaminanbank/<uuid:projekid>',documentviews.jaminanbankv, name="dokumen/jaminanbank"),
    path('dokumen/ppwjp/<uuid:projekid>',documentviews.pwjpview, name="dokumen/ppwjp"),
    path('dokumen/smrk/<uuid:projekid>',documentviews.smrkview, name="dokumen/smrk"),
    path('dokumen/skhas/<uuid:projekid>',documentviews.skhasview, name="dokumen/skhas"),
    path('dokumen/suratbon/<uuid:projekid>',documentviews.sbonview, name="dokumen/suratbon"),


    path('laporan/pdf/<uuid:projekid>', reportview.some_pdf, name="laporan/pdf"),
    path('laporan/excel/<uuid:projekid>', reportview.some_excel, name="laporan/excel"),
    path('laporan/filter', reportview.report_by_filter, name="laporan/filter"),
    path('laporan/excel', reportview.testexcel, name="laporan/excel"),
    path('laporan/excel2', reportview.testexcel2, name="laporan/excel2"),
    path('laporan/mrksatu/<uuid:projekid>', reportview.pdfmrksatu, name="laporan/mrksatu"),
    path('laporan/mrkdua/<uuid:projekid>',reportview.pdfmrkdua, name="laporan/mrkdua"),
    path('laporan/lsk/<uuid:projekid>',reportview.pdflsk, name="laporan/lsk"),
    path('laporan/mrktiga/<uuid:projekid>',reportview.pdfmrktiga, name="laporan/mrktiga"),
    path('laporan/psmk/<uuid:projekid>',reportview.pdfpsmk, name="laporan/psmk"),
    path('laporan/psk01/<uuid:projekid>', reportview.pdfpsksatu, name="laporan/psk01"),
    path('laporan/psk02/<uuid:projekid>', reportview.pdfpskdua, name="laporan/psk02"),
    path('laporan/senaraisemakan/<uuid:projekid>', reportview.ssemak, name="laporan/senaraisemakan"),
    path('laporan/jaminanbank/<uuid:projekid>', reportview.pdfjb, name="laporan/jaminanbank"),
    path('laporan/ppwjp/<uuid:projekid>', reportview.pdfppwjp, name="laporan/ppwjp"),

    path('laporan/smrk-01/<uuid:projekid>', reportview.pdfsmrksatu, name="laporan/smrk-01"),
    path('laporan/smrk-02/<uuid:projekid>', reportview.pdfsmrkdua, name="laporan/smrk-02"),

    path('laporan/skhas-01/<uuid:projekid>', reportview.pdfskhas01, name="laporan/skhas-01"),
    path('laporan/skhas-02/<uuid:projekid>', reportview.pdfskhas02, name="laporan/skhas-02"),

    path('laporan/spwjp-01/<uuid:projekid>', reportview.pdfpwjp01, name="laporan/spwjp-01"),
    path('laporan/spwjp-02/<uuid:projekid>', reportview.pdfpwjp02, name="laporan/spwjp-02"),

    path('sistem/subsistem', projekview.load_sistem, name="sistem/subsistem"),
    path('sistem/komponen', projekview.load_component, name="sistem/komponen"),

    path('login',authviews.loginJPS, name="login"),
    path('logout',authviews.logoutJPS, name='logout'),
    path('register',authviews.registerJPS, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
