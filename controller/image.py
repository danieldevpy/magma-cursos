from PIL import Image, ImageDraw, ImageFont
import io
from django.core.files.storage import default_storage

class ImageController:

    @classmethod
    def design_image(cls, img_certificate: Image.Image, img_pillow: Image.Image, x, y):
        """Adiciona uma imagem sobre outra em uma posição específica."""
        if not isinstance(img_certificate, Image.Image) or not isinstance(img_pillow, Image.Image):
            raise ValueError("Ambas as imagens devem ser objetos da classe PIL.Image.Image.")
        img_certificate.paste(img_pillow, (x, y))

    @classmethod
    def design_text(cls, image, value, pos_x, pos_y, size, color):
        """Desenha um texto na imagem na posição especificada, centralizado."""
        if not isinstance(image, Image.Image):
            raise ValueError("A imagem deve ser um objeto da classe PIL.Image.Image.")
        
        design = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size)

        # Usando textbbox para calcular a largura do texto
        text_bbox = design.textbbox((pos_x[0], pos_y), value, font=font)
        text_width = text_bbox[2] - text_bbox[0]  # Largura do texto
        center = (pos_x[0] + pos_x[1] - text_width) // 2  # Centralizando o texto

        design.text((center, pos_y), value, font=font, fill=color)

    @classmethod
    def get_bytes_from_path(cls, path: str):
        """Lê um arquivo da storage e retorna os bytes."""
        try:
            with default_storage.open(path, 'rb') as arquivo:
                return io.BytesIO(arquivo.read())
        except Exception as e:
            print(f"Erro ao ler o arquivo {path}: {e}")
            return None

    @classmethod
    def open_image_io(cls, img_bytes):
        """Abre a imagem a partir de um objeto de bytes."""
        if isinstance(img_bytes, bytes):
            return io.BytesIO(img_bytes)
        raise ValueError("img_bytes deve ser do tipo 'bytes'.")

    @classmethod
    def get_bytes_from_image(cls, image: Image, format, quality):
        """Converte uma imagem em um buffer de bytes no formato desejado."""
        if not isinstance(image, Image.Image):
            raise ValueError("O parâmetro 'image' deve ser um objeto da classe PIL.Image.Image.")
        
        if format == "JPEG":
            image = image.convert('RGB')  # Converte a imagem para RGB se for JPEG

        buffer = io.BytesIO()
        image.save(buffer, format=format, quality=quality)
        buffer.seek(0)  # Certifica-se de que o ponteiro do buffer esteja no início
        return buffer.read()

