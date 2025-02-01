from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional


class Experience(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    image = db.Column(db.String(255), nullable=True)


    country_id: Mapped[Optional[int]] = mapped_column(ForeignKey("country.id")) 
    country: Mapped[Optional["Country"]] = relationship(back_populates="experiences")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "country_id": self.country_id
        }
    
    @classmethod
    def from_dict(cls, experience_data):
        new_experience = cls(title=experience_data["title"], description=experience_data["description"], country_id=experience_data["country_id"])
        return new_experience