from django.db import models
from ..modelcontroller import kontraktor
from ..modelcontroller import dfnoperolehan
from django.contrib.auth.models import User

class Projek(models.Model):

    tajukkerja = models.CharField(max_length=50, null=True, blank=True)
    daerah = models.CharField(max_length=50, null=True, blank=True)
    pegawaiselia = models.ForeignKey(User, on_delete=models.CASCADE)
    nosebuthargalink = models.ForeignKey(dfnoperolehan.NoPerolehan, on_delete=models.CASCADE)

    def __str__(self):
        return self.tajukkerja
