import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.db.models import FileField

from gallery.models import Image

def create_image(location, days):
    time = timezone.now() + datetime.timedelta(days=days)
    #imgfile = FileField.save('test', ContentFile("test"), false)
    image = Image.objects.create(
            add_date=time, taken_date=timezone.now())
    image.imgfile.save('test', ContentFile("test"), False)
    return image

class ImageViewTest(TestCase):
    def test_index_view_with_no_image(self):
        response = self.client.get(reverse('gallery:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No images available")
        self.assertQuerysetEqual(response.context['latest_images'], [])

    def test_index_view_with_a_past_image(self):
        i = create_image("path", days=-30)
        response = self.client.get(reverse('gallery:index'))
        #self.assertQuerysetEqual(
        #        response.context['latest_images'], ['<Image: Image: path taken %s'%i.add_date]
        #)
        self.assertEqual(1, len(response.context['latest_images']))

    def test_index_view_with_a_future_image(self):
        i = create_image("path", days=30)
        response = self.client.get(reverse('gallery:index'))
        #self.assertQuerysetEqual(
        #        response.context['latest_images'], ['<Image: Image: path taken %s'%i.add_date]
        #)
        self.assertContains(response, "No images available", status_code=200)
        self.assertEqual(0, len(response.context['latest_images']))

    def test_index_view_with_a_future_and_past_image(self):
        f = create_image("future", days=30)
        p = create_image("past", days=-30)
        r = self.client.get(reverse('gallery:index'))
        self.assertEqual(1, len(r.context['latest_images']))

    def test_index_view_with_two_past_image(self):
        f = create_image("past1", days=-30)
        p = create_image("past2", days=-30)
        r = self.client.get(reverse('gallery:index'))
        self.assertEqual(2, len(r.context['latest_images']))


class ImageMethodTests(TestCase):
    def test_was_added_recently_with_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_image = Image(add_date=time)
        self.assertEqual(future_image.was_added_recently(), False)

    def test_was_added_with_old(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_image = Image(add_date=time)
        self.assertEqual(old_image.was_added_recently(), False)

    def test_was_added_with_recent(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_image = Image(add_date=time)
        self.assertEqual(recent_image.was_added_recently(), True)

class ImageIndexDetailTest(TestCase):
    def test_detail_view_with_a_future_image(self):
        image = create_image("path", days=30)
        response = self.client.get(reverse('gallery:detail', 
                args=(image.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_image(self):
        image = create_image("path", days=-30)
        response = self.client.get(reverse('gallery:detail', 
                args=(image.id,)))
        self.assertEqual(response.status_code, 200)
