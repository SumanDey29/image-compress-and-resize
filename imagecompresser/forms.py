from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    compression_percentage = forms.IntegerField(min_value=1, max_value=100)
