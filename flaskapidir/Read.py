from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    'postgresql://postgres:Skywill99@localhost:5432/mydb', echo=False)

test_data = pd.read_csv('./flaskapidir/uploads/test_data.csv')

test_data.to_sql('test_data', engine, if_exists='replace')

df = pd.read_sql_query('select * from test_data', con=engine)
print(df)
