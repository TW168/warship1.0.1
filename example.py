# example.py

import logging
from helpers.logging_config import setup_logging 
from helpers.config_helper import read_config
from helpers.mysql_utils import connect_to_mysql, fetch_data_from_mysql

setup_logging()
config = read_config("config/config.ini")
qry = f"select * from ipg_ez where site='AMJK' and product_group='SW'"
engine = connect_to_mysql(config)

df = fetch_data_from_mysql(engine, qry)
logging.info('Executed fetch_data_from_mysql(engine, qry)')
print(len(df))

