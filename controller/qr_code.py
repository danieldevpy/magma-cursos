import qrcode, io


class QrCodeController:

    @classmethod
    def make(cls, certificate):
        url = f'https://certificado.magmacursosltda.com.br/certificate/validate/{certificate.pk}'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        return img_bytes