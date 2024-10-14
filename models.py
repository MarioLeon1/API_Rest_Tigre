from sqlalchemy import Column, Integer, String
from database import Base

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    action = Column(String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'action': self.action
        }
