# pip install fpdf2

from fpdf import FPDF
from datetime import datetime

# -------------------------
# 1) Datos de ejemplo (simulan "bases de datos")
# -------------------------
DATASETS = [
    {
        "db_name": "Ventas_2025",
        "theme": "Ventas",
        "description": "Resumen mensual de ventas y desempeño comercial.",
        "kpis": {
            "Ingresos": 128500000,
            "Pedidos": 3421,
            "Ticket_promedio": 37550,
            "Crecimiento_%": 8.4
        },
        "rows": [
            {"Mes": "Ene", "Ingresos": 9500000, "Pedidos": 210, "Región": "Norte"},
            {"Mes": "Feb", "Ingresos": 10300000, "Pedidos": 245, "Región": "Centro"},
            {"Mes": "Mar", "Ingresos": 11000000, "Pedidos": 260, "Región": "Sur"},
        ],
    },
    {
        "db_name": "Riesgos_Territoriales",
        "theme": "Riesgo",
        "description": "Señales e indicadores de riesgo por zona priorizada.",
        "kpis": {
            "Alertas_activas": 27,
            "Zonas_priorizadas": 9,
            "Incidentes_mes": 41,
            "Variación_%": -3.2
        },
        "rows": [
            {"Zona": "Z1", "Alertas": 5, "Incidentes": 11, "Nivel": "Alto"},
            {"Zona": "Z2", "Alertas": 2, "Incidentes": 4, "Nivel": "Medio"},
            {"Zona": "Z3", "Alertas": 7, "Incidentes": 9, "Nivel": "Alto"},
        ],
    },
]

# -------------------------
# 2) PDF base
# -------------------------
class AutoReportPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, "Reporte automatizado (demo) - FPDF2", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 5, f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_draw_color(220, 220, 220)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)
        self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Página {self.page_no()}", align="C")
        self.set_text_color(0, 0, 0)

# -------------------------
# 3) Helpers para pintar secciones
# -------------------------
def money(n: float) -> str:
    # Ajusta a tu formato local
    return f"${n:,.0f}".replace(",", ".")

def add_section_title(pdf: FPDF, title: str):
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

def add_kpi_block(pdf: FPDF, kpis: dict):
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "KPIs", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)

    # Dos columnas simple
    col_w = (pdf.w - pdf.l_margin - pdf.r_margin) / 2
    items = list(kpis.items())

    for i, (k, v) in enumerate(items):
        label = str(k).replace("_", " ")
        if isinstance(v, (int, float)) and "ingres" in label.lower():
            value = money(v)
        else:
            value = f"{v}"

        pdf.cell(col_w, 6, f"{label}: {value}", border=1, new_x="RIGHT", new_y="TOP")
        # saltar línea cada 2 items
        if i % 2 == 1:
            pdf.ln(6)
    # si quedó impar, saltar línea
    if len(items) % 2 == 1:
        pdf.ln(6)

    pdf.ln(4)

def add_table(pdf: FPDF, rows: list[dict], title: str = "Muestra de datos", max_rows: int = 12):
    if not rows:
        return

    add_section_title(pdf, title)

    keys = list(rows[0].keys())
    usable_rows = rows[:max_rows]

    # Anchos: repartición simple (puedes mejorar esto a medida)
    available_w = pdf.w - pdf.l_margin - pdf.r_margin
    col_w = available_w / len(keys)

    # Header tabla
    pdf.set_font("Helvetica", "B", 10)
    for k in keys:
        pdf.cell(col_w, 7, str(k), border=1, align="C")
    pdf.ln(7)

    # Filas
    pdf.set_font("Helvetica", "", 10)
    for r in usable_rows:
        for k in keys:
            pdf.cell(col_w, 7, str(r.get(k, "")), border=1)
        pdf.ln(7)

    pdf.ln(4)

def add_db_page(pdf: FPDF, dataset: dict):
    """
    1 dataset = 1 página
    """
    pdf.add_page()

    # Título principal de la página (tema + nombre base)
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 9, f"Tema: {dataset['theme']}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, f"Fuente: {dataset['db_name']}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(4)

    # Descripción
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 6, dataset.get("description", ""))
    pdf.ln(4)

    # KPIs
    add_kpi_block(pdf, dataset.get("kpis", {}))

    # Tabla de muestra
    add_table(pdf, dataset.get("rows", []), title="Muestra (primeras filas)")

# -------------------------
# 4) Generación (la parte importante: iterar)
# -------------------------
def build_report(datasets: list[dict], output_path: str = "reporte_demo.pdf"):
    pdf = AutoReportPDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)

    # Portada opcional
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "Reporte Automatizado", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 7, "Demo: una página por base de datos, generada iterando datasets.", align="C")
    pdf.ln(8)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 7, "Contenido:", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    for i, d in enumerate(datasets, 1):
        pdf.cell(0, 6, f"{i}. {d['theme']} ({d['db_name']})", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    # Páginas por dataset
    for dataset in datasets:
        add_db_page(pdf, dataset)

    pdf.output(output_path)
    return output_path

if __name__ == "__main__":
    out = build_report(DATASETS, "reporte_demo.pdf")
    print("OK ->", out)