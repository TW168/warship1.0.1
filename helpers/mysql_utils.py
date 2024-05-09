# helpers/mysql_uitls.py

import logging
from sqlalchemy import create_engine
import pandas as pd

def connect_to_mysql(config):
    try:
        db_username = config['MYSQL']['Username']
        db_password = config['MYSQL']['Password']
        db_host = config['MYSQL']['Host']
        db_port = config['MYSQL']['Port']
        db_name = config['MYSQL']['Database']

        # Creating connection string
        connection_string = f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

        # Creating SQLAlchemy engine
        engine = create_engine(connection_string)

        logging.info("Connected to MySQL database successfully.")
        return engine
    except Exception as e:
        logging.error(f"Error connecting to MySQL database: {e}")
        return None

def fetch_data_from_mysql(engine, query):
    """
    Fetches data from a MySQL database using the provided SQLAlchemy engine and SQL query.

    Args:
        engine (sqlalchemy.engine.base.Engine): SQLAlchemy engine connected to the MySQL database.
        query (str): SQL query to execute.

    Returns:
        pandas.DataFrame or None: DataFrame containing the fetched data if successful, None otherwise.
    """
    try:
        # Using Pandas to execute SQL query and fetch data
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        logging.error(f"Error fetching data from MySQL database: {e}")
        return None