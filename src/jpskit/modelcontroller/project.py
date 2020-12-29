from django.db import models
from ..modelcontroller import kontraktor
class Projek(models.Model):

    title = models.CharField(max_length=50, null=True, blank=True)
    tarikh = models.CharField(max_length=50, null=True, blank=True)
    vendor = models.ForeignKey(kontraktor.Kontraktor, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
