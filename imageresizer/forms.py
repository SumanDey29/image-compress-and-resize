from django import forms

class ImageResizeForm(forms.Form):
    image = forms.ImageField()
    ASPECT_RATIOS = [
        ('4:3', '4:3'),
        ('16:9', '16:9'),
        ('1:1', '1:1'),
        ('3:2', '3:2'),
        ('custom', 'Custom'),
    ]
    aspect_ratio = forms.ChoiceField(choices=ASPECT_RATIOS, required=True)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        aspect_ratio = cleaned_data.get('aspect_ratio')
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')

        if aspect_ratio == 'custom' and (not width or not height):
            raise forms.ValidationError("Width and height are required for custom aspect ratio.")
        return cleaned_data