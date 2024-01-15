"""Video List Model."""
# table vide_list
# id (primary key)
# name (big string)
# opened (true false)
from sqlalchemy import Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column

from config import DB_PREFIX, Base


class VideoList(Base):
    """Video List Model."""

    __tablename__ = f"{DB_PREFIX}_video_list"
    id: Mapped[int] = mapped_column(primary_key=True)
    _name: Mapped[str] = mapped_column(
        "name", Text, nullable=False, unique=True)
    _opened: Mapped[bool] = mapped_column("opened", Boolean, default="false")

    @property
    def name(self) -> str:
        """Get name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set name."""
        self._name = value

    @property
    def opened(self) -> bool:
        """Get opened."""
        return self._opened

    @opened.setter
    def opened(self, value: bool) -> None:
        """Set opened."""
        self._opened = value
