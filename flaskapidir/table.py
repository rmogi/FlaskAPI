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

# Read
# セッションを張る
Session = sessionmaker(bind=engine)
session = Session()

# まずSQL文を作る
sql = session.query(Profile).\
    filter(2 <= Profile.id).\
    filter(Profile.id <= 4)

# データの取得
for row in session.query(Profile).all():
    print(row.id, row.birthday, row.birthplace)

#
"""
# Create
# INSERT死体データを作っておく
user_profile = [
    (1, '1992/2/11', 'Aichi'),
    (2, '1988/1/14', 'Miyagi'),
    (3, '2002/6/16', 'Yamaguchi'),
    (4, '1996/8/5', 'Osaka'),
    (5, '1972/12/25', 'Nagasaki'),
]

# データを1つずつ読み出して、Profileクラスに格納

for data in user_profile:
    profile = Profile()
    profile.id = data[0]
    profile.birthday = data[1]
    profile.birthplace = data[2]

    session.add(profile)    # INSERT

session.commit()            # コミットしないとデータベースには反映されない

# データ確認
for row in session.query(Profile).all():
    print(row.id, row.birthday, row.birthplace)

# 問い合わせを発行する
# for row in session.query(Users).all():
 #   print(row.id, row.name, row.age)
"""
