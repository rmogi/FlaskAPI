from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATE
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://postgres:Skywill99@localhost:5432/mydb',
    echo=False)

# テーブル定義のベース
Base = declarative_base()


class Test_data(Base):
    __tablename__ = 'test_data'

    PassengerId = Column(Integer, primary_key=True)
    Pclass = Column(Integer)
    Name = Column(String(50)
    Sex=Column(String(10))
    Age=olumn(float)
    SibSp=Column(Integer)
    Parch=Column(Integer)
    Ticket=Column(Integer)
    Fare=Column(float)
    Cabin=Column(Integer)
    Embarked=Column(String)


# セッションを張る
Session=sessionmaker(bind=engine)
session=Session()

# 問い合わせを発行する
# for row in session.query(Users).all():
#   print(row.id, row.name, row.age)

# データ確認
for row in session.query(Test_data).all():
    print(row.PassengerId, row.Pclass, row.Name,
          row.Sex, row.Age, row.SibSp, row.Parch,
        row.Ticket, row.Fare, row.Cabin, row.Embarked)
