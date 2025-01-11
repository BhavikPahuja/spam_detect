from django.shortcuts import render
from .models import QR_genration
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO
import hashlib
import vt

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


def link_detection(request):
    if request.method == "POST":
        # Initialize the VirusTotal client
        client = vt.Client("480e3b4565c3444d7c425e3832ab21a4ee55fbbf9738ea3385108e0d1e6b9177")
        link = request.POST.get('link')  # Get the link from the POST request

        try:
            # Get the URL ID for the provided link
            url_id = vt.url_id(link)
            # Fetch the URL object from VirusTotal
            url_object = client.get_object(f"/urls/{url_id}")
            
            # Access the `last_analysis_stats` dictionary
            analysis_stats = url_object.last_analysis_stats
            print(type(analysis_stats))  # Debug: Check the type of the stats

            # Render the link details in the template
            return render(request, "link_detection.html", {"link_details": analysis_stats,"url":link})
        except Exception as e:
            print(f"Error: {e}")  # Log the error for debugging purposes
            return render(request, "link_detection.html", {"error": "An error occurred while processing the link."})
    return render(request, "link_detection.html")