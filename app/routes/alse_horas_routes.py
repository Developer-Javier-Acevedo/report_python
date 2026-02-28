from flask import Blueprint, jsonify

from app.services.alse_horas_service import list_alse_horas ,get_alse_horas_by_id

alse_horas = Blueprint("alse_horas", __name__)


def _serialize_alse_horas(row):
    return {
        "id_alse_horas": int(row.id_alse_horas) if row.id_alse_horas is not None else None,
        "id_alse_biografia": int(row.id_alse_biografia) if row.id_alse_biografia is not None else None,
        "id_req_hora": int(row.id_req_hora) if row.id_req_hora is not None else None,
        "cant_anual": int(row.cant_anual) if row.cant_anual is not None else None,
        "cant_pp": int(row.cant_pp) if row.cant_pp is not None else None,
        "cant_sp": int(row.cant_sp) if row.cant_sp is not None else None,
        "comentarios": row.comentarios,
        "usuario_creador": row.usuario_creador,
        "fecha_creacion": row.fecha_creacion.isoformat() if row.fecha_creacion else None,
        "usuario_modificador": row.usuario_modificador,
        "fecha_modificacion": row.fecha_modificacion.isoformat() if row.fecha_modificacion else None,
        "ejc_version": int(row.ejc_version) if row.ejc_version is not None else None,
    }


@alse_horas.route("/alse-horas", methods=["GET"])
def get_alse_horas():
    rows = list_alse_horas()
    return jsonify([_serialize_alse_horas(row) for row in rows]), 200

@alse_horas.route("/alse-horas/<int:id_alse_horas>", methods=["GET"])
def get_alse_horas_by_id_route(id_alse_horas):
    row = get_alse_horas_by_id(id_alse_horas)
    if not row:
        return jsonify({"message": "Registro no encontrado"}), 404

    return jsonify(_serialize_alse_horas(row)), 200

