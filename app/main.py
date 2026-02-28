import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv(override=True)

from flask import Flask
from flask_cors import CORS
from app.routes.healthcheck import healthcheck
app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])
app.register_blueprint(healthcheck, url_prefix="/api/sicca")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
