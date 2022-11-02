# Python SQLAlchemy + Alembic example

### Just run
```sh
python3 -m pip install -r requirements.txt
python3 app.py
```

File named `db.sqlite3` will be created. Check contents with `sqlitebrowser` or something.

### Step by step, create from scratch
1. Create and activate venv
```sh
python3 -m venv ./.venv/alembic
source ./.venv/alembic/bin/activate
```

2. Install alembic and sqlalchemy
```sh
python3 -m pip install alembic
python3 -m pip install sqlalchemy
```

3. Init alembic
```
python3 -m alembic init alembic
```

4. Change alembic .ini files
- set `sqlalchemy.url`
```ini
sqlalchemy.url = sqlite:///./db.sqlite3
```

- add to `env.py`
```py
# New import
from main import Base

# set target_metadata
target_metadata = Base.metadata
```

5. Edit `main.py`, init sqlalchemy, and make models.
```py
# Creating models

...

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

...
```

6. Make autogenerate migrations and upgrade database schema
```sh
python3 -m alembic revision --autogenerate -m 'init'
python3 -m alembic upgrade head
```

7. Everytime you want to sync table fields automatically with model changes, do this:
- Update model, we add `timestamp` to `SnapshotRecord`
```py
@dataclass
class SnapshotRecord(Base):
    __tablename__ = 'snapshot_record'

    id: int = Column(Integer, primary_key=True)
    camera_id: int  = Column(Integer)
    timestamp: str  = Column(String)
```
- Revision
```sh
python3 -m alembic revision --autogenerate -m 'add timestamp to snapshot record'
```
- Upgrade
```sh
python3 -m alembic upgrade head
```

8. Add running script (test add SnapshotRecord and Camera like in main.py) and just run
```sh
python3 main.py
```

Ref: 
Alembic tutorial: https://alembic.sqlalchemy.org/en/latest/tutorial.html
Alembic autogeneration guide: https://alembic.sqlalchemy.org/en/latest/autogenerate.html