from django.contrib import admin
from .modelcontroller import project, order, kontraktor, dfnoperolehan, userprofile,document

admin.site.register(kontraktor.Kontraktor)
admin.site.register(userprofile.UserProfile)
admin.site.register(dfnoperolehan.NoPerolehan)
admin.site.register(project.Projek)
admin.site.register(document.MRKSatu)
admin.site.register(document.MRKKursus)
admin.site.register(document.MRKDua)
admin.site.register(document.Laporansiapkerja)
admin.site.register(document.MRKTiga)
admin.site.register(project.isSungai)
admin.site.register(project.sistem)
admin.site.register(project.subsistem)


# Register your models here.
