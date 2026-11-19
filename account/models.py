from django.db import models

# Create your models here.
class Subject(models.Model):
    name=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    code=models.IntegerField()

    def __str__(self):
        return self.name
  