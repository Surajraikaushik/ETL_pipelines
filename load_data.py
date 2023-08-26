# create a table and load the category value
import Transform_data as td
import Db_Conn2 as dc
import pandas as pd
def create_table(table_name):
    g =td.transf()
    print('length after remove duplicates ---- '+ str(len(g)))
    g.to_sql(table_name, con=dc.cnx, if_exists='replace', index=False)

    query = "select * from " + table_name
    df = pd.read_sql_query(query, con=dc.cnx)
