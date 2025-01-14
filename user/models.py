from django.db import models

class QR_genration(models.Model):
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='qr/')  # QR codes will be stored in the 'media/qr/' directory

    def __str__(self):
        return self.link

class UploadedFile(models.Model):
    file = models.FileField(upload_to='file_detection/')
    uploaded_at = models.DateTimeField(auto_now_add=True)




class url_shortener(models.Model):
    original_url = models.URLField(max_length=200)
    shorten_url = models.URLField(max_length=200)

    def __str__(self):
        return self.original_url
    

class link_detection(models.Model):
    url = models.URLField(max_length=200)
    malicious = models.CharField(max_length=50)
    suspicious = models.CharField(max_length=50)
    undetected = models.CharField(max_length=50)
    harmless = models.CharField(max_length=50)
    timeout = models.CharField(max_length=50)

    def __str__(self):
        return self.url

import datetime

class Contact(models.Model):
    name = models.URLField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        ObjName = f"{self.name} {self.phone} {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        return ObjName

    