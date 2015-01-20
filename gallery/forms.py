from django import forms

class ImageForm(forms.Form):
    imgfile = forms.FileField(
        label = 'Select an image file',
        help_text = 'max. 42 megabytes')
    title = forms.CharField(
        label='Give it a title',
        help_text = 'max. 100 chars')
