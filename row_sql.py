from sqlalchemy import create_engine, inspect, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

URL = "mysql+mysqlconnector://aluno:aluno123@localhost/orm"

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)


def main():
    engine = create_engine(url=URL)
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


    Session = sessionmaker(engine)
    with Session.begin() as session:
        lucas = Pessoa(nome="Lucas Venezian Povoa")
        session.add(lucas)
    with Session.begin() as session:
        lucas = Pessoa(nome="meu nome nome")
        session.add(lucas)


if __name__ == "__main__":
    main()
