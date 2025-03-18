from django.core.files.storage import default_storage
import io
from PIL import ImageFont, ImageDraw, Image

class ImageController:

    @classmethod
    def design_image(cls, img_certificate: Image.Image, img_pillow: Image.Image, x, y):
        img_certificate.paste(img_pillow, (x, y))

    @classmethod
    def design_text(cls, image, value, pos_x, pos_y, size, color):
        design = ImageDraw.Draw(image)
        font = ImageFont.truetype('src/arial.ttf',  size)
        text_size = design.textlength(value, font)
        center = (pos_x[0] + pos_x[1] - text_size) // 2
        design.text((center, pos_y), value, font=font, fill=color)

    @classmethod
    def get_bytes_from_path(cls, path: str):
        with default_storage.open(path, 'rb') as arquivo:
            return io.BytesIO(arquivo.read())
    
    @classmethod
    def open_image_io(cls, img_bytes):
        return io.BytesIO(img_bytes)
        
    @classmethod
    def get_bytes_from_image(cls, image: Image, format, quality):
        if format == "JPEG":
            image = image.convert('RGB') 
        buffer = io.BytesIO()
        image.save(buffer, format=format, quality=quality)
        buffer.seek(0)
        return buffer.read()