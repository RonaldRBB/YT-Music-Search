"""Video List Model."""
from datetime import datetime
from sqlalchemy import Boolean, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

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
