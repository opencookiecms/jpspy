from django.db import models

class Project:
    def __init__(self, title, name):
        self.title = title
        self.name = name

    def projectdata(self, **kwarg):
        self.title = models.CharField(max_length=50, null=True, blank=True)
        self.name = models.CharField(max_length=50, null=True, blank=True)

        return self
