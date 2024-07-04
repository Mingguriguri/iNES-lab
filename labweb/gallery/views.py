from django.shortcuts import render
from .models import Gallery

def ai_gallery(request):
    photos = Gallery.objects.all().order_by('-upload_date')
    photos = Gallery.objects.filter(team='AI')
    return render(request, 'labweb/gallery/ai_gallery.html',
                  {
                      'Gallery': photos
                  })

def hw_gallery(request):
    photos = Gallery.objects.all().order_by('-upload_date')
    photos = Gallery.objects.filter(team='HW')
    return render(request, 'labweb/gallery/hw_gallery.html',
                  {
                      'Gallery': photos
                  })
