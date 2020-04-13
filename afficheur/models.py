from django.db import models

# Create your models here.


class City(models.Model):

    search = models.CharField(max_length=1000000000,null=True)

    def __str__(self):
        return self.search

    class Meta:
        verbose_name_plural = "resumes"
