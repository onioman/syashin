from django.shortcuts import render, get_object_or_404

from gallery.models import Image

def index(request):
    latest_images = Image.objects.order_by('-taken_date')[:5]
    context = {'latest_images' : latest_images}
    return render(request, 'gallery/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/image_full.html', {'image' : image })
