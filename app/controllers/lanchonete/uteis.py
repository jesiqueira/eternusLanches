import secrets
import os
from flask import current_app
from PIL import Image


def salvarImagem(form_imagem):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_imagem.filename)
    imagem_fn = random_hex + f_ext
    imagem_path = os.path.join(current_app.root_path, 'static/img/lanches', imagem_fn)

    output_size = (360, 225)
    i = Image.open(form_imagem)
    i.thumbnail(output_size)
    i.save(imagem_path)

    return imagem_fn
