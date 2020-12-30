from django.contrib import admin
from .modelcontroller import project, order, kontraktor, dfnoperolehan, userprofile

admin.site.register(kontraktor.Kontraktor)
admin.site.register(userprofile.UserProfile)
admin.site.register(dfnoperolehan.NoPerolehan)
admin.site.register(project.Projek)


# Register your models here.
