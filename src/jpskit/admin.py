from django.contrib import admin
from .modelcontroller import project, order, kontraktor, dnoperolehan, userprofile

admin.site.register(kontraktor.Kontraktor)
admin.site.register(userprofile.UserProfile)
admin.site.register(dnoperolehan.NoPerolehan)
admin.site.register(project.Projek)


# Register your models here.
