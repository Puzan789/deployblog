from django.db import models

# Create your models here.
class project(models.Model):
    message = models.CharField(max_length=40, null=False)
    image = models.ImageField(upload_to="images", null=False)

    def __str__(self):
        return self.message
