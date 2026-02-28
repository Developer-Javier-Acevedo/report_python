# Arquitectura

## Vision general

El proyecto ahora esta orientado a un backend Flask que expone datos para un frontend de reportes.

## Responsabilidades por capa

### Flask backend
- Configuracion
- Conexion Oracle
- Servicios de negocio
- Endpoints JSON

### Frontend
- Visualizacion del reporte
- Filtros
- Exportacion a PDF

## Flujo actual

```text
HTTP request
  -> Flask routes
    -> services
      -> connectors
        -> db/session
          -> settings
            -> .env
```

## Decision arquitectonica

La exportacion PDF se deja fuera del backend para que:
- el frontend controle la presentacion final
- el backend se concentre en datos y reglas de negocio
- no se duplique logica entre web y PDF
