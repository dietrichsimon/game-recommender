from sqlalchemy import create_engine
from recommender.config import AWS_PW, HOST
from recommender import config
import pandas as pd
#from config import AWS_PW

# specify sqlalchemy connection string
#host = 'spiced.csdsa4ecozd8.eu-central-1.rds.amazonaws.com'
#user = 'simon'
host = config.HOST
user = config.USER

port = '5432'
#pw = AWS_PW
pw = config.AWS_PW
dbname='boardgames'
conns = f'postgres://{user}:{pw}@{host}:{port}/{dbname}'

# connect to database
db = create_engine(conns, encoding='latin1', echo=False)

# read in db as DataFrame
def db_to_df(db_table):
    '''Reads in a table from the board games database as pandas DataFrame'''
    query = f"SELECT * FROM {db_table};"
    pd_table = pd.read_sql(query, db)
    return pd_table
