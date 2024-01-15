"""Script para migrar la base de datos."""
from sqlalchemy import text

from app.models import (
    VideoList
)
from config import (
    Base,
    engine,
    session,
)


def test_connection():
    """Prueba la conexión a la base de datos."""
    with engine.connect() as conn:
        result = conn.execute(text("select 'Conexión establecida'"))
        print(f" * {result.all()}")


def create_tables(drop_all=True):
    """Crea las tablas de la base de datos."""
    if drop_all:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def main():
    """Función principal."""
    test_connection()
    create_tables(drop_all=True)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
