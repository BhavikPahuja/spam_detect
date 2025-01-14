from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('qr',views.qr,name='qr'),
    path('link_detection',views.link_detection,name='link_detection'),
    path('file_detection',views.file_detection,name='file_detection'),
    path('url_shortener', views.shorten_url, name='shorten_url'),
    path('send_email', views.send_email, name='send_email'),
    path('anonymous_mail', views.anonymous_mail, name='anonymous_mail'),
    path('contact', views.contact, name='contact'),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)