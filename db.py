# INSERT INTO  usesr (nombre, edad, genero) VALUES ("elvis", 10 , "masculino")
# UPDATE INTO  users (nombre, edad, genero) VVALUES ("elvis", 10 , "masculino") WHERE  name == elvis
# SELECT * FROM users WHERE edad = 10

from sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()

class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key = True)
    nombres = Column(String, nullable = False)
    apellido = Column(String, nullable = False)
    carnet = Column(Integer, nullable = False)

    @hybrid_property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellido}"

class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key = True)
    curso = Column(String)
    nota = Column(Integer)
    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
   # alumnos = relationship("Alumno" , back_populates = "notas")

engine = create_engine("sqlite:///:memory:")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

lucia = Alumno(
    nombres= "lucia",
    apellido= "gomez",
    carnet= 1234,
)

print(lucia.id)
session.add(lucia)
session.commit()
session.refresh(lucia)
print(lucia.id)

#query


lucia_from_db = session.query(Alumno).where(Alumno.nombres == "lucia").first()
print(lucia_from_db.apellido)

#update
lucia_from_db.carnet = 5678
session.add(lucia_from_db)
session.commit()

#delete 
#session.delete(lucia)
#session.commit()


luis = Alumno(
    nombres= "luis",
    apellido= "lopez",
    carnet= 5656,
)
session.add(luis)
session.commit()

alumnos = session.query(Alumno).all()
print(alumnos[0].nombres)
print(alumnos[1].nombres) 

print(luis.nombre_completo)