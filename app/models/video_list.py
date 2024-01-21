"""Video List Model."""
from datetime import datetime
from sqlalchemy import Boolean, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import re

from config import DB_PREFIX, Base


class VideoList(Base):
    """Video List Model."""

    __tablename__ = f"{DB_PREFIX}_video_list"
    id: Mapped[int] = mapped_column(primary_key=True)
    _folder: Mapped[str] = mapped_column("folder", Text, nullable=False)
    _name: Mapped[str] = mapped_column(
        "name", Text, nullable=False, unique=True)
    _created_at: Mapped[datetime] = mapped_column(
        "created_at", DateTime, nullable=False, default=None)
    _opened: Mapped[bool] = mapped_column("opened", Boolean, default="false")

    @property
    def folder(self) -> str:
        """Get folder."""
        return self._folder

    @folder.setter
    def folder(self, value: str) -> None:
        """Set folder."""
        self._folder = value

    @property
    def name(self) -> str:
        """Get name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set name."""
        self._name = value
        self.__format_name()

    @property
    def created_at(self) -> datetime:
        """Get created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime) -> None:
        """Set created_at."""
        self._created_at = value

    @property
    def opened(self) -> bool:
        """Get opened."""
        return self._opened

    @opened.setter
    def opened(self, value: bool) -> None:
        """Set opened."""
        self._opened = value
    # private function delete extensions

    def __format_name(self):
        """Funcion treat_name."""
        self.__delete_res_from_name()
        self.__delete_fps_from_name()
        self.__delete_audio_from_name()

    def __delete_res_from_name(self):
        """Funcion delete_res_from_name."""
        self._name = re.sub(r'[^a-zA-Z)\]]?\d{3,4}p[\W_-]?', r'', self._name)

    def __delete_fps_from_name(self):
        """Funcion delete_fps_from_name."""
        self._name = re.sub(r'[^a-zA-Z)\]]?\d{1,3}fps[\W_-]?', r'', self._name)

    def __delete_audio_from_name(self):
        """Funcion delete_fps_from_name."""
        self._name = re.sub(
            r'[^a-zA-Z)\]]?(AV1|H264|VP9|H.264)[\W_-]?', r'', self._name)
        self._name = re.sub(
            r'[^a-zA-Z)\]]?(LQ)?[^a-zA-Z)\]]?\d{3,4}kbit[\W_-]?', r'', self._name)
        self._name = re.sub(
            r'[^a-zA-Z)\]]?(AAC|AAC_2|Opus|Vorbis)[\W_-]?', r'', self._name)
