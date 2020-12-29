from django.db import models

class Projek(models.Model):

    title = models.CharField(max_length=50, null=True, blank=True)
    tarikh = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.first_name
