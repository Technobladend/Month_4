from django.db import models

class TVParser(models.Model):
    title_url = models.CharField(max_length=255)
    title_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to='parser')

    def __str__(self):
        return self.title_name