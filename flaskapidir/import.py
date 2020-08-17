from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Date(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class test_data(Base):
    # SQLAlchemyにテーブル名を伝え、テーブル固有の引数がある場合はそれについて知っておく必要があります。
    __tablename__ = 'test_data'
    # SQLAlchemyに列の名前とその属性を伝えます

    PassengerId = Column(Integer, primary_key=True)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String)
    Age = Column(Integer)
    SibSp = Column(Integer)
    Parch = Column(Integer)
    Ticket = Column(Integer)
    Fare = Column(Float)
    Cabin = Column(String)
    Embarked = Column(String)

if __name__ == "__main__":
    t = time()

    engine = create_engine(
    'postgresql://postgres:ryou1198@localhost:5432/mydb',
    echo=False)
    Base.metadata.create_all(engine)

    session = sessionmaker
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "test_data.csv"

        data = Load_Date(file_neme)

        for i in data:
            record = test_data(**{
                'Pclass' : i[0],
                'Name' : i[1],
                'Sex' : i[2],
                'Age' : i[3],
                'SibSp' : i[4],
                'Parch' : i[5],
                'Ticket' : i[6],
                'Fare' : i[7],
                'Cabin' : i[8],
                'Embarked' : i[9]
            })
            s.add(record)

        s.commit()
    except:
        s.rollback()
    finally:
        s.close()
    