"""Script para buscar videos."""
import os
import urllib
import webbrowser

from app.models import VideoList
from config import session


def get_video_list():
    """Funcion get_video_list."""
    print("Buscando videos...")
    video_list = session.query(
        VideoList
    ).filter(
        VideoList._folder == 'varios', VideoList._opened == False
    ).order_by(
        VideoList._created_at
    ).all()
    return video_list


def open_url(video_name):
    """Funcion open_url."""
    url = f"www.youtube.com/watch?v={urllib.parse.quote_plus(video_name)}"
    webbrowser.open(url)


def run():
    """Funcion run."""
    video_list = get_video_list()
    i = 0
    for video in video_list:
        print(f"{i} : {video.name}")
        open_url(video.name)
        video.opened = True
        i += 1
        if i == 20:
            key = input("Conitnua? enter | close q | close no save n: ")
            if key == '':
                session.commit()
                i = 0
            elif key == 'q':
                session.commit()
                session.close()
                break
            elif key.lower() == 'n':
                session.rollback()
                session.close()
                break


def main():
    """Funcion main."""
    print("Open Urls")
    run()


if __name__ == "__main__":
    main()
