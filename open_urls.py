"""Script para buscar videos."""
import os
import webbrowser

from app.models import VideoList
from config import session


def run():
    """Funcion run."""
    video_list = session.query(VideoList).filter(
        VideoList._folder == 'varios').order_by(VideoList._created_at).all()
    i = 0
    for video in video_list:
        video_name = os.path.splitext(video.name)[0]
        print(video_name)
        open_url(video_name)
        video.opened = True
        i += 1
        if i == 10:
            key = input("Conitnua? enter/n: ")
            if key == '':
                session.commit()
                i = 0
            elif key.lower() == 'n':
                session.rollback()
                session.close()
                break


def open_url(video_name):
    """Funcion open_url."""
    webbrowser.open(
        f"https://www.youtube.com/results?search_query={
            video_name.replace(' ', '+')}"
    )


def main():
    """Funcion main."""
    webbrowser.open("link")
    run()


if __name__ == "__main__":
    main()
