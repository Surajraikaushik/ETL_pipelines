import Db_Conn2 as dc
import pandas as pd

def read_src(Table_name):
    query = "SELECT * FROM " + Table_name
    df = pd.read_sql_query(query , con=dc.cnx)
    print('length without duplicate-------' + str(len(df)))

    return df

