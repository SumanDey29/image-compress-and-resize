from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .compressor import compress_image
from .forms import ImageUploadForm
import os

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            compression_percentage = form.cleaned_data['compression_percentage']

            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)

            input_image_path = os.path.join(fs.location, filename)
            output_image_name = f"compressed_{filename}"
            output_image_path = os.path.join(fs.location, output_image_name)

            compress_image(input_image_path, output_image_path, compression_percentage)

            compressed_file_url = fs.url(output_image_name)

            original_size = round(int(os.path.getsize(input_image_path))/1024, 2)
            compressed_size = round(int(os.path.getsize(output_image_path))/1024, 2)

            return render(request, 'upload_success.html', {
                'uploaded_file_url': uploaded_file_url,
                'compressed_file_url': compressed_file_url,
                'original_size': original_size,
                'compressed_size': compressed_size,
            })
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


