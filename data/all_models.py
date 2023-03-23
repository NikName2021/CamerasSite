import datetime
import os

import sqlalchemy
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.engine import URL
from dotenv import load_dotenv

DeclBase = declarative_base()


class BreakCamers(DeclBase):
    __tablename__ = 'break_camers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_camera = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    street = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.String)
    timestamp = sqlalchemy.Column(sqlalchemy.DateTime,
                                  default=datetime.datetime.now)
    anomal = relationship("Anomal")

    def main(self):
        return sorted(self.anomal, key=lambda x: x.chance, reverse=True)[0]

    def serialize(self):
        return {
            'id': self.id,
            'id_camera': self.id_camera,
            'street': self.street,
            'image': 'http://localhost/static/working/bad_640/' + self.image,
            'timestamp': self.timestamp,
            'breakdown': self.main().breakdown,
            'chance': self.main().chance
        }


class Anomal(DeclBase):
    __tablename__ = 'anomals'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    breakdown = sqlalchemy.Column(sqlalchemy.String)
    chance = sqlalchemy.Column(sqlalchemy.REAL)
    break_camera_id = sqlalchemy.Column(sqlalchemy.Integer,
                                        ForeignKey('break_camers.id'))


if __name__ == '__main__':
    load_dotenv()
    db_path = URL.create(
        drivername="postgresql",
        username=os.getenv("POSTGRES_USER"),
        host="localhost",
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DATABASE"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    engine = create_engine(db_path)
    DeclBase.metadata.create_all(engine)
