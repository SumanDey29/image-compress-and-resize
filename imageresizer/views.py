from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from PIL import Image
from .forms import ImageResizeForm

def resize_image(input_image_path, output_image_path, width, height):
    with Image.open(input_image_path) as img:
        img = img.resize((width, height), Image.LANCZOS)
        img.save(output_image_path)

def upload_resize_image(request):
    if request.method == 'POST':
        form = ImageResizeForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            aspect_ratio = form.cleaned_data['aspect_ratio']
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']

            # Handle aspect ratio
            if aspect_ratio != 'custom':
                original_width, original_height = Image.open(image).size
                if aspect_ratio == '4:3':
                    width = original_width
                    height = int(original_width * 3 / 4)
                elif aspect_ratio == '16:9':
                    width = original_width
                    height = int(original_width * 9 / 16)
                elif aspect_ratio == '1:1':
                    width = min(original_width, original_height)
                    height = width
                elif aspect_ratio == '3:2':
                    width = original_width
                    height = int(original_width * 2 / 3)

            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)

            output_image_path = fs.path('resized_' + filename)
            resize_image(fs.path(filename), output_image_path, width, height)
            resized_file_url = fs.url('resized_' + filename)

            context = {
                'original_size': image.size,
                'resized_size': Image.open(output_image_path).size,
                'uploaded_file_url': uploaded_file_url,
                'resized_file_url': resized_file_url,
            }
            return render(request, 'upload_resize_success.html', context)
    else:
        form = ImageResizeForm()
    return render(request, 'upload_resize.html', {'form': form})
