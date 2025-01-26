from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional

class Expirience(db.model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]


    country_id: Mapped[Optional[int]] = mapped_column(ForeignKey("country.id")) 
    board: Mapped[Optional["Country"]] = relationship(back_populates="expiriences")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "country_id": self.country_id
        }
    
    @classmethod
    def from_dict(cls, expirience_data):
        new_expirience = cls(title=expirience_data["title"], description=expirience_data["description"], country_id=expirience_data["country_id"])
        return new_expirience