# Ejecucion

## Requisitos previos

Necesitas:
- Python 3.12 o compatible
- Acceso a Oracle
- Credenciales validas

## Paso 1. Crear entorno virtual

```powershell
python -m venv .venv
```

## Paso 2. Activar entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

## Paso 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

## Paso 4. Configurar `.env`

```env
DB_HOST=localhost
DB_PORT=1521
DB_SERVICE=ORCLCDB
DB_USER=report_user
DB_PASSWORD=change_me
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
FLASK_DEBUG=true
API_PREFIX=/api
OUTPUT_DIR=output
```

## Paso 5. Ejecutar Flask

```powershell
python -m app.main
```

## URLs disponibles

- `http://127.0.0.1:5000/api/`
- `http://127.0.0.1:5000/api/health`

## Resultado esperado en salud

```json
{
  "oracle_connection": true
}
```

## Nota sobre PDF

En esta arquitectura el backend no genera el PDF.
La exportacion queda reservada para el frontend.
