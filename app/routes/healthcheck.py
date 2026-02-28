from flask import Blueprint, jsonify
from sqlalchemy import create_engine, text
from config.config import Config

healthcheck = Blueprint('api/sicca', __name__)


@healthcheck.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"}), 200


@healthcheck.route('/db-check', methods=['GET'])
def db_check():
    try:
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, **Config.SQLALCHEMY_ENGINE_OPTIONS)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1 FROM DUAL")).scalar()
        return jsonify({"status": "ok", "oracle_result": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 500



