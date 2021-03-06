from django.contrib import admin
from .modelcontroller import project, order, kontraktor, dfnoperolehan, userprofile,document, kursus

admin.site.register(kontraktor.Kontraktor)
admin.site.register(userprofile.UserProfile)
admin.site.register(dfnoperolehan.NoPerolehan)
admin.site.register(project.Projek)
admin.site.register(project.KDvot)
admin.site.register(document.MRKSatu)
admin.site.register(document.MRKKursus)
admin.site.register(document.MRKDua)
admin.site.register(document.Laporansiapkerja)
admin.site.register(document.MRKTiga)
admin.site.register(document.PSK)
admin.site.register(document.SenaraiSemakan)
admin.site.register(document.PSMK)
admin.site.register(document.SuratPJaminanbank)
admin.site.register(document.Perakuanpwjp)
admin.site.register(document.kosprojek)
admin.site.register(project.isSungai)
admin.site.register(project.sistem)
admin.site.register(project.subsistem)
admin.site.register(kursus.Course)
admin.site.register(kursus.Attandance)



# Register your models here.
