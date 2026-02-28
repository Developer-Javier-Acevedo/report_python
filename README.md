# report_python

Backend base en Flask para construir un sistema de reportes conectado a Oracle 19 y a APIs externas, dejando la visualizacion y la exportacion del reporte al frontend.

## Enfoque actual

- El backend en Flask expone datos y servicios via REST
- El frontend consume esos datos
- El frontend muestra el reporte web
- El frontend controla la exportacion o impresion a PDF

Esto permite que la logica de negocio viva en el backend y la experiencia visual quede en el frontend.

## Estado actual

Implementado:
- Conexion a Oracle 19 con `oracledb` (modo thin, sin Oracle Client) + `SQLAlchemy 2.x`
- Configuracion lazy via `.env` con `load_dotenv(override=True)` para que el reloader de Flask siempre lea valores frescos
- Blueprint `api/sicca` con prefijo `/api/sicca`
- Endpoint de salud `/ping`
- Endpoint de validacion Oracle `/db-check` (ejecuta `SELECT 1 FROM DUAL`)

Pendiente:
- Endpoints de negocio reales
- Repositorios Oracle por entidad
- Integraciones con APIs externas
- Frontend del reporte
- Exportacion PDF desde el frontend

## Estructura actual

```text
report_python/
|-- app/
|   |-- main.py                      # Entry point Flask (puerto 8000)
|   |-- config/
|   |   `-- config.py                # Config con _LazyURI descriptor
|   |-- models/
|   |   `-- manufacturer_model.py    # Modelo SQLAlchemy: Fabricante
|   |-- routes/
|   |   `-- manufacturer_routes.py   # Blueprint /api/sicca
|   `-- services/
|       |-- __init__.py
|       `-- manufacturer_service.py  # Fabrica de sesiones DB
|-- docs/
|-- .env
|-- requirements.txt
`-- README.md
```

## Dependencias principales

```text
SQLAlchemy>=2.0.0
oracledb>=1.4.0
Flask>=3.0.0
python-dotenv==1.0.1
flask-cors
```

## Configuracion `.env`

```env
# Oracle Database
DB_HOST=<ip-del-servidor>
DB_PORT=<puerto-listener>
DB_SERVICE=<nombre-servicio>
DB_USER=<usuario>
DB_PASSWORD=<contrasena>

# Flask
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
FLASK_DEBUG=true
API_PREFIX=/api
OUTPUT_DIR=output
```

> **Nota:** se usa `DB_SERVICE` (nombre de servicio Oracle), no `DB_NAME`.

## Ejecucion

### 1. Crear entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 3. Configurar `.env`

Completa tus credenciales Oracle en el archivo `.env` de la raiz del proyecto.

### 4. Ejecutar el backend Flask

```powershell
python app/main.py
```

El servidor levanta en `http://0.0.0.0:8000`.

> **Importante:** ejecutar siempre desde la raiz del proyecto (`d:\report_python`), no desde dentro de `app/`.

### 5. Probar los endpoints

```powershell
# Health check
curl http://localhost:8000/api/sicca/ping

# Validar conexion Oracle
curl http://localhost:8000/api/sicca/db-check
```

Respuestas esperadas:

```json
{ "status": "ok" }
```

```json
{ "status": "ok", "oracle_result": 1 }
```

## Arquitectura

### Backend Flask
Responsable de:
- Exponer endpoints REST
- Consultar Oracle 19 via `oracledb` thin mode
- Integrar APIs externas
- Consolidar datos para el frontend

### Frontend (pendiente)
Responsable de:
- Mostrar reportes en web
- Aplicar filtros y vistas
- Exportar o imprimir a PDF

## Decisiones tecnicas

| Decision | Detalle |
|---|---|
| `oracledb` thin mode | No requiere Oracle Instant Client instalado en la maquina |
| `_LazyURI` descriptor | El URI de BD se construye en cada acceso a `Config.SQLALCHEMY_DATABASE_URI`, no al importar el modulo, para evitar leer env vars antes de `load_dotenv()` |
| `load_dotenv(override=True)` | Garantiza que el reloader de Flask siempre use los valores actuales de `.env` |
| Imports sin prefijo `src.` | Los modulos dentro de `app/` se importan directamente (`from config.config import Config`). El `sys.path` se ajusta en `main.py` |
| Puerto 8000 | CORS habilitado para `http://localhost:4200` (Angular dev server) |

## Siguiente evolucion recomendada

1. Crear `repositories/` con consultas Oracle por entidad
2. Crear endpoints como `/api/sicca/reports/...`
3. Separar la sesion DB con un patron de inyeccion (evitar crear engine por request)
4. Crear frontend en Angular, React o Vue
5. Implementar exportacion PDF desde el frontend con la API de impresion del navegador
