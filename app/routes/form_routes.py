import io
from flask import Blueprint, send_file
from app.services.prueba import build_form_pdf_bytes

form_bp = Blueprint("form", __name__)


@form_bp.route("/formulario-uas", methods=["GET"])
def descargar_formulario_uas():
    pdf_bytes = build_form_pdf_bytes()
    buffer = io.BytesIO(pdf_bytes)
    buffer.seek(0)
    return send_file(
        buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="formulario_uas_rpas.pdf",
    )
