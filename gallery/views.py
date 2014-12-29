from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from gallery.models import Image

def index(request):
    latest_images = Image.objects.order_by('-taken_date')[:5]
    context = {'latest_images' : latest_images}
    return render(request, 'gallery/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/image_full.html', {'image' : image })

def change(request, image_id):
    i = get_object_or_404(Image, pk=image_id)
    try:
        i.location = request.POST['location']
    except:
        return render(request, 'gallery/image_full.html', {
            'image' : i,
            'error_message': "Wrong location",
        })
    else:
       i.save() 
       return HttpResponseRedirect(reverse('gallery:detail', args=(image_id,)))
