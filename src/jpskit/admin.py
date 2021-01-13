from django.contrib import admin
from .modelcontroller import project, order, kontraktor, dfnoperolehan, userprofile,document

admin.site.register(kontraktor.Kontraktor)
admin.site.register(userprofile.UserProfile)
admin.site.register(dfnoperolehan.NoPerolehan)
admin.site.register(project.Projek)
admin.site.register(document.MRK1)


# Register your models here.
