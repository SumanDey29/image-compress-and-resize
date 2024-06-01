from PIL import Image

def compress_image(input_image_path, output_image_path, quality):
    with Image.open(input_image_path) as img:
        if img.mode in ("RGBA", "LA"):
            img = img.convert("RGB")
        img.save(output_image_path, format="JPEG", quality=quality, optimize=True)