from sqlalchemy import Column, Date, Numeric, String

from app.models.manufacturer_model import Base


class AlseHoras(Base):
    __tablename__ = "EJC_ALSE_HORAS"
    __table_args__ = {"schema": "SICCA"}

    id_alse_horas = Column("ID_ALSE_HORAS", Numeric(15, 0), primary_key=True, nullable=False)
    id_alse_biografia = Column("ID_ALSE_BIOGRAFIA", Numeric(15, 0), nullable=False)
    id_req_hora = Column("ID_REQ_HORA", Numeric(15, 0), nullable=True)
    cant_anual = Column("CANT_ANUAL", Numeric(4, 0), nullable=True)
    cant_pp = Column("CANT_PP", Numeric(4, 0), nullable=True)
    cant_sp = Column("CANT_SP", Numeric(4, 0), nullable=True)
    comentarios = Column("COMENTARIOS", String(4000), nullable=True)
    usuario_creador = Column("USUARIO_CREADOR", String(30), nullable=True)
    fecha_creacion = Column("FECHA_CREACION", Date, nullable=True)
    usuario_modificador = Column("USUARIO_MODIFICADOR", String(30), nullable=True)
    fecha_modificacion = Column("FECHA_MODIFICACION", Date, nullable=True)
    ejc_version = Column("EJC_VERSION", Numeric(22, 0), nullable=True, default=0)
