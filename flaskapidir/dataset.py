from sqlalchemy import create_engine
import pandas as pd


def database_set():
    # データベースに接続
    engine = create_engine(
        'postgresql://postgres:Ry0u1198@localhost:5432/mydb', echo=True)

    i = pd.read_csv('uploads/test_data.csv')
    i.to_sql('test_data', engine, if_exists='replace')

    a = pd.read_sql_query('select * from test_data', con=engine)
