'''Connection to database'''

import pandas as pd
from sqlalchemy import create_engine

from recommender import config

# specify sqlalchemy connection string
HOST = config.HOST
USER = config.USER
PORT = "5432"
PW = config.AWS_PW
DBNAME = "boardgames"
CONNS = f"postgres://{USER}:{PW}@{HOST}:{PORT}/{DBNAME}"

# connect to database
DB = create_engine(CONNS, encoding="latin1", echo=False)

# read in db as DataFrame
def db_to_df(db_table):
    """Reads in a table from the board games database as pandas DataFrame"""
    query = f"SELECT * FROM {db_table};"
    pd_table = pd.read_sql(query, DB)
    return pd_table
