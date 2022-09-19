from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base

URL = "mysql+mysqlconnector://aluno:aluno123@localhost"

Base = declarative_base()

class Pessoa():
    pass



def main():
    engine = create_engine(url=URL)

    insp = inspect(engine)
    db_list = insp.get_schema_names()
    print(db_list)
    with engine.connect() as connection:
        result_set = connection.execute("SHOW DATABASES")
        for row in result_set:
            print(row[0])

if __name__ == "__main__":
    main()
