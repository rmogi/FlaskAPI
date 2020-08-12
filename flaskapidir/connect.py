from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATE
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://postgres:Skywill99@localhost:5432/mydb',
    echo=False)

# テーブル定義のベース
Base = declarative_base()

# ユーザーを登録するテーブル


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# ユーザーの誕生日と出身地を登録するテーブル


class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer,
                ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'),
                primary_key=True)
    birthday = Column(DATE)
    birthplace = Column(String(50))


Base.metadata.create_all(bind=engine)

# セッションを張る
Session = sessionmaker(bind=engine)
session = Session()

# 問い合わせを発行する
for row in session.query(Users).all():
    print(row.id, row.name, row.age)
