from sqlalchemy.orm import Mapped, mapped_column, relationship 
from ..db import db
from app.models.experience import Experience


class Country(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    visited: Mapped[bool]
    borned: Mapped[bool]
    want_to_visit: Mapped[bool]
    experiences: Mapped[list["Experience"]] = relationship(back_populates="country")

    def to_dict(self):
        return {
            "id": self.id,
            "visited": self.visited,
            "borned": self.borned,
            "want_to_visit": self.want_to_visit,
        }
    
    @classmethod
    def from_dict(cls, country_data):
        new_country = cls(visited=country_data["visited"], borned=country_data["borned"], want_to_visit=country_data["want_to_visit"])
        return new_country