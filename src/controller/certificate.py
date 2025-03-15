from certificate.models import Certificate
from controller.image import ImageController
from controller.qr_code import QrCodeController
from model.models import Text
from PIL import Image
from dataclasses import dataclass

@dataclass
class ImageBytes:
    front: bytes
    back: bytes

class CertificateController:
    color_default = (0, 0, 0)

    @classmethod
    def make(cls, certificate: Certificate, format = "PNG", quality = 100, qr_code = False) -> ImageBytes:
        front = Image.open(ImageController.get_bytes_from_path(certificate.model.front.name))
        back = Image.open(ImageController.get_bytes_from_path(certificate.model.back.name))
        data_json = certificate.get_json()

        for key, value in data_json.items():
            text = certificate.model.texts.filter(field=key).first()

            if text:
                color = tuple(map(int, text.color.split(',')))
                ImageController.design_text(front, value.upper(), text.get_pos_x(), text.pos_y, text.size, color)

        if qr_code:
            qr_code_img = Image.open(QrCodeController.make(certificate))
            w = 40
            h = 40
            ImageController.design_image(front, qr_code_img, w, h)

        img_bytes = ImageBytes(
            front=ImageController.get_bytes_from_image(front, format, quality),
            back=ImageController.get_bytes_from_image(back, format, quality)
        )
  
        return img_bytes