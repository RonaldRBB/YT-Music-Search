"""Crea la base de datos."""
from migrations.migrator import main as migrate


def main():
    """Crea la base de datos."""
    migrate()


if __name__ == "__main__":
    main()
