# pip install fpdf2

from fpdf import FPDF
from datetime import datetime

# -------------------------
# Config del formulario (ajusta a tu necesidad)
# -------------------------
FORM_TITLE = "FORMULARIO DE\nREGISTRO UAS/RPAS"
ORG_LINES = [
    "MINISTERIO DE DEFENSA NACIONAL",
    "COMANDO GENERAL FUERZAS MILITARES",
    "EJÉRCITO NACIONAL",
    "DIVISIÓN DE AVIACIÓN ASALTO AÉREO",
]

FORM_CODE = "FO-JEMOP-DAVAA-XXXX"   # ajusta
FORM_VERSION = "0"                 # ajusta
FORM_ISSUE_DATE = "XXXX-XX-XX"     # ajusta (o pon datetime.now().strftime("%Y-%m-%d"))

TOTAL_PAGES = 3  # <- lo que pediste: tres hojas exactas


# -------------------------
# PDF base estilo formulario
# -------------------------
class UASFormPDF(FPDF):
    def header(self):
        # Márgenes y posiciones
        left = self.l_margin
        top_y = 10
        page_w = self.w - self.l_margin - self.r_margin

        # Caja derecha (Página / Código / Versión / Fecha)
        box_w = 70
        box_x = self.w - self.r_margin - box_w
        box_y = top_y
        box_h = 30

        # Bloque izquierdo (organización + título)
        left_w = page_w - box_w - 6  # espacio entre bloques

        # --- Bloque institucional (izquierda) ---
        self.set_xy(left, top_y)
        self.set_font("Helvetica", "B", 10)
        for line in ORG_LINES:
            self.cell(left_w, 5, line, ln=1, align="C")

        self.ln(1)
        self.set_font("Helvetica", "B", 14)
        # Título en 2 líneas
        for tline in FORM_TITLE.split("\n"):
            self.set_x(left)
            self.cell(left_w, 7, tline, ln=1, align="C")

        # --- Caja derecha (borde) ---
        self.set_draw_color(0, 0, 0)
        self.rect(box_x, box_y, box_w, box_h)

        self.set_font("Helvetica", "", 9)

        # Fila 1: Página X de Y
        self.set_xy(box_x + 2, box_y + 2)
        self.cell(18, 5, "Página:", border=0)
        self.cell(10, 5, str(self.page_no()), border=0, align="R")
        self.cell(8, 5, "de", border=0, align="C")
        self.cell(10, 5, str(TOTAL_PAGES), border=0, align="L")

        # Línea separadora dentro de la caja
        self.line(box_x, box_y + 9, box_x + box_w, box_y + 9)

        # Fila 2: Código
        self.set_xy(box_x + 2, box_y + 11)
        self.cell(18, 5, "Código:", border=0)
        self.cell(box_w - 20, 5, FORM_CODE, border=0)

        # Fila 3: Versión
        self.set_xy(box_x + 2, box_y + 17)
        self.cell(18, 5, "Versión:", border=0)
        self.cell(box_w - 20, 5, str(FORM_VERSION), border=0)

        # Fila 4: Fecha de emisión
        self.set_xy(box_x + 2, box_y + 23)
        self.cell(30, 5, "Fecha de emisión:", border=0)
        self.cell(box_w - 32, 5, str(FORM_ISSUE_DATE), border=0)

        # Línea inferior del encabezado (separador general)
        self.set_draw_color(180, 180, 180)
        self.line(self.l_margin, 45, self.w - self.r_margin, 45)

        # Posición donde empieza el contenido
        self.set_y(50)
        self.set_text_color(0, 0, 0)

    def footer(self):
        # En el Word el número va arriba (en el header),
        # entonces aquí dejamos el footer limpio.
        pass


# -------------------------
# Helpers para contenido (placeholders)
# -------------------------
def add_page_1(pdf: FPDF):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "SECCIÓN 1 (Hoja 1): Datos generales / Identificación", ln=1)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6,
        "- Aquí pones los campos del formulario (ej: responsable, unidad, fecha, etc.)\n"
        "- Puedes dibujar líneas, cajas o tablas según el formato que quieras replicar."
    )

def add_page_2(pdf: FPDF):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "SECCIÓN 2 (Hoja 2): Información técnica UAS/RPAS", ln=1)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6,
        "- Aquí pones los campos técnicos (modelo, fabricante, sistema lanzamiento, recuperación, etc.)\n"
        "- Puedes usar tablas como en tu ejemplo anterior si lo necesitas."
    )

def add_page_3(pdf: FPDF):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "SECCIÓN 3 (Hoja 3): Adjuntos / Observaciones / Firmas", ln=1)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6,
        "- Aquí pones el checklist de adjuntos, observaciones y firma.\n"
        "- Si necesitas numeración de ítems como el Word, lo armamos con tablas/celdas."
    )


# -------------------------
# Generación del PDF (3 páginas fijas)
# -------------------------
def build_form_pdf(output_path: str = "formulario_uas_rpas.pdf"):
    pdf = UASFormPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)

    # Importante: 3 hojas exactas
    add_page_1(pdf)
    add_page_2(pdf)
    add_page_3(pdf)

    pdf.output(output_path)
    return output_path


def build_form_pdf_bytes() -> bytes:
    """Genera el PDF en memoria y retorna los bytes, sin tocar el disco."""
    pdf = UASFormPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    add_page_1(pdf)
    add_page_2(pdf)
    add_page_3(pdf)
    return bytes(pdf.output())


if __name__ == "__main__":
    out = build_form_pdf("formulario_uas_rpas.pdf")
    print("OK ->", out)