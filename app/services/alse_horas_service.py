from app.models.alse_horas_model import AlseHoras
from app.services.manufacturer_service import get_session


def list_alse_horas():
    session = get_session()
    try:
        return session.query(AlseHoras).all()
    finally:
        session.close()

def get_alse_horas_by_id(id_alse_horas: int):
    session = get_session()
    try:
        return session.query(AlseHoras)\
            .filter(AlseHoras.id_alse_horas == id_alse_horas)\
            .first()
    finally:
        session.close()
