from django.contrib import admin
from .modelcontroller import project, order, kontraktor, dfnoperolehan, userprofile,document

admin.site.register(kontraktor.Kontraktor)
admin.site.register(userprofile.UserProfile)
admin.site.register(dfnoperolehan.NoPerolehan)
admin.site.register(project.Projek)
admin.site.register(document.MRK1)
admin.site.register(project.isSungai)
admin.site.register(project.sistem)
admin.site.register(project.subsistem)


# Register your models here.
