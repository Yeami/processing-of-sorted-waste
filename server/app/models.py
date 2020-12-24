from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)

    class Meta:
        db_table = 'roles'
