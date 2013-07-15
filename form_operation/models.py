from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title
