import os


class _LazyURI:
    """Descriptor que lee os.getenv cada vez que se accede, no en tiempo de import."""
    def __get__(self, obj, owner):
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '1521')
        service = os.getenv('DB_SERVICE')
        return f"oracle+oracledb://{user}:{password}@{host}:{port}/?service_name={service}"


class Config:
    SQLALCHEMY_DATABASE_URI = _LazyURI()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 5,
        "max_overflow": 5,
        "pool_timeout": 30,
        "pool_recycle": 1800,
        "pool_pre_ping": True,
    }
