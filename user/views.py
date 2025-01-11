from django.shortcuts import render
from .models import QR_genration
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO
import hashlib

def home(request):
    return render(request, 'home.html')


def qr(request):
    if request.method == "POST":
        link_for_qr = request.POST.get("input_link")

        # Generate the QR code
        qr_image = qrcode.make(link_for_qr)

        # Save the QR code to an in-memory file
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Generate a sanitized filename using a hash
        sanitized_filename = hashlib.md5(link_for_qr.encode()).hexdigest()[:10] + "_qr.png"

        # Create a new QR_genration object
        qr_instance = QR_genration(link=link_for_qr)
        qr_instance.image.save(sanitized_filename, ContentFile(buffer.read()), save=True)
        buffer.close()

        # Fetch all QR codes from the database
        objects = QR_genration.objects.all()

        return render(request, 'qr.html', {'objects': objects})
    
    # Render the template for GET requests
    return render(request, 'qr.html')