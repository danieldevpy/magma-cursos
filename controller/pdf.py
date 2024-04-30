import io
from controller.certificate import ImageBytes
from reportlab.pdfgen import canvas
from PIL import Image


class PDFController:
    

    @classmethod
    def make(cls, img_bytes = ImageBytes):
        front = Image.open(io.BytesIO(img_bytes.front))
        back = Image.open(io.BytesIO(img_bytes.back))
        page_width = max(front.width, back.width)
        page_height = max(front.height, back.height)
        pdf_buffer = io.BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=(page_width, page_height))
        c.drawInlineImage(front, 0, 0, width=front.width, height=front.height)
        c.showPage()
        c.drawInlineImage(back, 0, 0, width=back.width, height=back.height)
        c.save()
        return pdf_buffer.getvalue()