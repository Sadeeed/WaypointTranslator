from django.db import models


class WaypointFile(models.Model):
    file = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)
