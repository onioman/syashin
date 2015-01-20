from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic

from gallery.models import Image,Album
from gallery.forms import ImageForm

def index(request):
    # add the post thing?

    images = Image.objects.filter(add_date__lte=timezone.now()
            ).order_by('-taken_date')
    albums = Album.objects.all()
    image_form = ImageForm()
    context = {'images' : images, 'albums' : albums, 
            'image_form' : image_form }
    return render(request, 'gallery/index.html', context)

def imageCreate(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        new_image = Image.create(request.FILES['imgfile'], request.POST['title'])
        new_image.save()
        return HttpResponseRedirect(reverse('gallery:index'))

def albumIndex(request, album_id):
    albums = Album.objects.all()
    album = get_object_or_404(Album, pk=album_id)
    images = album.images.all()
    context = {
            'images' : images,
            'albums' : albums,
            'album'  : album
            }
    return render(request, 'gallery/index.html', context)

def albumCreate(request):
    album = Album()
    album.name = request.POST['name']
    album.save()
    image_ids = request.POST['images'].split(',')
    for image_id in image_ids:
        image = get_object_or_404(Image, pk=image_id)
        album.images.add(image)
    return HttpResponseRedirect(reverse('gallery:albumIndex', args=(album.id,)))

def albumRemoveImage(request, album_id, image_id):
    album = get_object_or_404(Album, pk=album_id)
    image = get_object_or_404(Image, pk=image_id)
    album.images.remove(image)
    album.save()
    return HttpResponseRedirect(reverse('gallery:albumIndex', args=(album.id,)))

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'images'

    def get_queryset(self):
        return Image.objects.filter(add_date__lte=timezone.now()
                ).order_by('-taken_date')[:5]

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id, add_date__lte=timezone.now())
    print image
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
