from django.db import models

class QR_genration(models.Model):
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='qr/')  # QR codes will be stored in the 'media/qr/' directory

    def __str__(self):
        return self.link

class UploadedFile(models.Model):
    file = models.FileField(upload_to='file_detection/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


import string
import random

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=6, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"
