from dotenv import load_dotenv
import os
from sqlmodel import Session , create_engine  , SQLModel

load_dotenv()

connection_string = os.getenv('db_conn_str')

engine = create_engine(connection_string , echo=True)

print(engine)


def get_Session():
    with Session(engine) as session:
        yield session

def create_db_table():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_table()