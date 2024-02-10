# Import libraries
import psycopg2
import logging
from traceback import format_exc
from psycopg2 import OperationalError
from psycopg2 import sql
from configparser import ConfigParser

# ? Logger basic settings
logging.basicConfig(
    level=logging.DEBUG,
    filename="./code/log/workshop001.log",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s",
)
parser = ConfigParser()

# Connection data for PostgreSQL
credentials_filename = "./code/config/credentials.ini"
database_section = "postgresql"
# ? In [credentials_filename] the structure is:
# ? - Section: [database_section]
# ?     - option 'host': localhost (default)
# ?     - option 'database': etl_workshop_first
# ?     - option 'default_database': postgres
# ?     - option 'user': postgres (default)
# ?     - option 'password': '' (default)
# ?     - option 'port': 5432 (default)


class Connection_Postgres:
    """Create connection with PostgreSQL"""
