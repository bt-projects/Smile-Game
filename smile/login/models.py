from django.db import models

# Create your models here.

class DemoSmile(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'demo_smile'