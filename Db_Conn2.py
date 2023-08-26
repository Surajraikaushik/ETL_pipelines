from sqlalchemy import create_engine
import pandas
#    conn = psycopg2.connect(database="Sample_Data", user="postgres", password="Abhi@123", host="127.0.0.1", port="5432")

# Postgres username, password, and database name
POSTGRES_ADDRESS = '127.0.0.1' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'postgres' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES USERNAME
POSTGRES_PASSWORD = "Abhi123" ## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD
POSTGRES_DBNAME = 'Sample_Data' ## CHANGE THIS TO YOUR DATABASE NAME


# A long string that contains the necessary Postgres login information
postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME,
password=POSTGRES_PASSWORD,
ipaddress=POSTGRES_ADDRESS,
port=POSTGRES_PORT,
dbname=POSTGRES_DBNAME))

# Create the connection
cnx = create_engine(postgres_str)
#df = pandas.read_sql_query('SELECT * FROM products', con=cnx)
#print(df.columns.values)