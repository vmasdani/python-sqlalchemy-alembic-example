from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Integer, Column, String, create_engine
import datetime
import json
import dataclasses
from dataclasses import dataclass
from typing import  Text 
import time
import pprint
import sys

Base = declarative_base()
engine = create_engine("sqlite:///./db.sqlite3", echo=True, future=True)

@dataclass
class Camera(Base):
    __tablename__ = 'camera'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

@dataclass
class SnapshotRecord(Base):
    __tablename__ = 'snapshot_record'

    id: int = Column(Integer, primary_key=True)
    camera_id: int  = Column(Integer)
    timestamp: str = Column(String)

if sys.argv[1] == 'exec':
    print('Inserting camera:')
    c1 = Camera()
    c1.name = f'Camera {datetime.datetime.now()}'

    session = Session(engine)
    session.add(c1)

    session.commit()

    print('Inserting snapshot')
    s1 = SnapshotRecord()
    s1.camera_id = c1.id
    s1.timestamp = f'{datetime.datetime.now()}'
    session.add(s1)

    s2 = SnapshotRecord()
    s2.camera_id = c1.id
    s2.timestamp = f'{datetime.datetime.now()}'
    session.add(s2)

    session.commit()

    print()
    print('Inserted camera:')
    print(json.dumps(dataclasses.asdict(c1), indent=4))

    print()
    print('Inserted sessions:')
    print(json.dumps(dataclasses.asdict(s1), indent=4))
    print(json.dumps(dataclasses.asdict(s2), indent=4))

