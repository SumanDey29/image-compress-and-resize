from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    compressed_image = models.ImageField(upload_to='compressed/', null=True, blank=True)
    compression_percentage = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
