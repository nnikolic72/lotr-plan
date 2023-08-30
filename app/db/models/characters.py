from sqlalchemy import Column, Integer, String

import settings


class Character(settings.Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    health = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)
    armor = Column(Integer, nullable=False)
    focus = Column(Integer, nullable=False)
    resistance = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    block = Column(Integer, nullable=False)
    critical_chance = Column(Integer, nullable=False)
    evasion = Column(Integer, nullable=False)
