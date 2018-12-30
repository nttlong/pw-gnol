from django.db.models import Model
from django.db import models
class LanguageResource(Model):
    Language = models.CharField(max_length=2)
    AppName = models.CharField(max_length=100)
    ViewName = models.CharField(max_length=400)
    Key = models.CharField()
    Value = models.CharField()
    class Meta:
        db_table = 'sys_languages'
        unique_together = (("Language", "AppName","ViewName","Key"),)