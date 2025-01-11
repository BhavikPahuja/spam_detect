from django.db import models

class QR_genration(models.Model):
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='qr/')  # QR codes will be stored in the 'media/qr/' directory

    def __str__(self):
        return self.link
