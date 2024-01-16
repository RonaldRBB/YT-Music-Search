"""Script para buscar videos."""
import os
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from app.models import VideoList
from config import FILES_PATH, session


def get_sorted_files(directory):
    """Funcion get_sorted_files."""
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return sorted(file_paths, key=lambda f: os.path.getmtime(f))


def process_files(directory):
    """Funcion process_files."""
    files = get_sorted_files(directory)
    for file in files:
        print("=" * 50)
        print(file)
        folder_name = os.path.basename(os.path.dirname(file))
        file_name = os.path.basename(file)
        video = VideoList(
            folder=folder_name,
            name=file_name,
            created_at=datetime.fromtimestamp(os.path.getmtime(file)),
            opened=False
        )
        try:
            session.add(video)
            session.commit()
        except IntegrityError:
            print("Video already exists")
            session.rollback()


def main():
    """Funcion main."""
    process_files(FILES_PATH)


if __name__ == "__main__":
    main()
