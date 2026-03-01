import sys
import os
_app_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_app_dir)
sys.path.insert(0, _app_dir)      # permite: from config.config / from routes.xxx
sys.path.insert(0, _project_root) # permite: from app.routes.xxx / from app.services.xxx

from dotenv import load_dotenv
load_dotenv(override=True)

from flask import Flask
from flask_cors import CORS
from app.routes.alse_horas_routes import alse_horas
from app.routes.healthcheck import healthcheck
from app.routes.form_routes import form_bp
app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])
app.register_blueprint(healthcheck, url_prefix="/api/sicca")
app.register_blueprint(alse_horas, url_prefix="/api/sicca")
app.register_blueprint(form_bp, url_prefix="/api/sicca")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
