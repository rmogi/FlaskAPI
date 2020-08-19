from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql://postgres:ryou1198@localhost:5432/mydb',
    echo=False)

# コネクションを張ります
print("===コネクション===")
connection = engine.connect()
for row in connection.execute('SELECT * FROM users'):
    print(row.id, row.name, row.age)
connection.close()

# セッションを張ります
print("===セッション===")
Session = sessionmaker(bind=engine)
session = Session()
for row in session.execute('SELECT * FROM users'):
    print(row.id, row.name, row.age)
session.close()