from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from gallery.models import Image

def index(request):
    latest_images = Image.objects.order_by('-taken_date')[:5]
    template = loader.get_template('gallery/index.html')
    context = RequestContext(request, {
        'latest_images' : latest_images,
    })
    return HttpResponse(template.render(context))

def detail(request, image_id):
    return HttpResponse("You're looking at image: %s." % image_id)

# Create your views here.
