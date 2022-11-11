from django.db import models

class Tareas(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField

    def _str_(self):
        return f"{self.title} {self.description}"
