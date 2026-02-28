# Modulos

## `app/__init__.py`
Crea la aplicacion Flask y registra rutas.

## `app/main.py`
Punto de entrada para ejecutar el servidor Flask.

## `app/routes.py`
Define los endpoints HTTP actuales.

Endpoints:
- `GET /api/`
- `GET /api/health`

## `app/config/settings.py`
Lee `.env` y expone configuracion de Oracle y Flask.

## `app/db/base.py`
Clase base ORM de SQLAlchemy.

## `app/db/session.py`
Crea el `engine` y `SessionLocal`.

## `app/connectors/oracle_client.py`
Valida conectividad Oracle.

## `app/services/report_service.py`
Contiene la logica de negocio actual del healthcheck.
