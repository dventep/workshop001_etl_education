# Import libraries
import psycopg2
import logging
from traceback import format_exc
from psycopg2 import OperationalError
from psycopg2 import sql
from configparser import ConfigParser

#? Logger basic settings
logging.basicConfig(level=logging.DEBUG, filename='code/workshop001.log', encoding='utf-8', format='%(asctime)s - %(levelname)s - %(message)s')
parser = ConfigParser()

# Connection data for PostgreSQL
credentials_filename = 'code/credentials.ini'
database_section = 'postgresql'
# ? In [credentials_filename] the structure is:
# ? - Section: [database_section]
# ?     - option 'host': localhost (default)
# ?     - option 'database': etl_workshop_first
# ?     - option 'default_database': postgres
# ?     - option 'user': postgres (default)
# ?     - option 'password': '' (default)
# ?     - option 'port': 5432 (default)

class Connection_Postgres ():
    """ Create connection with PostgreSQL """
    
    def __init__(self):
        """ Constructor """
        self.connection_config = False
        self.connection = False
        self.data_to_connection()
        
        if self.connection_config:
            self.create_connection_postgresql()

    def data_to_connection (self):
        """ Method to get credentials data to connect with database """
        parser.read(credentials_filename)

        connection_config = {}
        if parser.has_section(database_section):
            params = parser.items(database_section)
            for param in params:
                connection_config[param[0]] = param[1]
        else:
            raise Exception(f'Section {database_section} not found in {credentials_filename} file.')
        self.connection_config = connection_config
        
    def create_connection_postgresql(self):
        """ Method to create a connection with database """
        try:
            postgre_connection = psycopg2.connect(
                dbname = self.connection_config['default_database'],
                user = self.connection_config['user'],
                password = self.connection_config['password'],
                host = self.connection_config['host'],
                port = self.connection_config['port']
            )
            postgre_connection.autocommit = True
            exist_database = True
            
            cursor = postgre_connection.cursor()
            logging.info(f'Connected to the PostgreSQL server with {self.connection_config["default_database"]} DB.')

            # Verificate whether the workshop database exists
            cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"),
                            ( self.connection_config['database'],))
            exist_database = cursor.fetchone()

            if not exist_database:
                #  Create etl_workshop_first database
                cursor.execute(f'CREATE DATABASE {self.connection_config["database"]}')
                postgre_connection.close()
                # Create the structure of database for this workshop
                self.create_structure_database()
            else:
                self.create_connection_database()
            logging.info(f"Connected with {self.connection_config['database']} - user: {self.connection_config['user']}")
                        
        except (psycopg2.DatabaseError, Exception) as error:
            logging.error(error, exc_info=True)
            
    def log(self, text):
        """ Method to create log records """
        logging.info(text)

    def create_connection_database(self):
        """ Method to create a connection with database """
        # Create connection with etl_workshop_first database
        self.connection = psycopg2.connect(
            dbname = self.connection_config['database'],
            user = self.connection_config['user'],
            password = self.connection_config['password'],
            host = self.connection_config['host'],
            port = self.connection_config['port']
        )
        self.connection.autocommit = True

    def close_connection_database(self):
        """ Method to close connection with database """
        if self.connection:
            self.connection.close()

    def create_structure_database(self):
        """ Method to create all necessary structure for the database """
        # Connect with created etl_workshop_first database
        self.create_connection_database()
        cursor = self.connection.cursor()

        # Create table 'applicant' if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS applicant (
                first_name VARCHAR DEFAULT NULL,
                last_name VARCHAR DEFAULT NULL,
                email VARCHAR DEFAULT NULL,
                applicant_date DATE DEFAULT NULL,
                applicant_year INTEGER DEFAULT NULL,
                applicant_month INTEGER DEFAULT 0,
                applicant_month_name VARCHAR DEFAULT NULL,
                country VARCHAR DEFAULT NULL,
                experience_year INTEGER DEFAULT 0,
                seniority VARCHAR DEFAULT NULL,
                technology VARCHAR DEFAULT NULL,
                code_challenge_score INTEGER DEFAULT 0,
                technical_interview_score INTEGER DEFAULT 0,
                is_hire INTEGER DEFAULT 0 CHECK (is_hire >= 0 AND is_hire <= 1)
            )
        """)
        # Create table 'raw_applicant' if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS raw_applicant (
                first_name VARCHAR DEFAULT NULL,
                last_name VARCHAR DEFAULT NULL,
                email VARCHAR DEFAULT NULL,
                applicant_date VARCHAR DEFAULT NULL,
                country VARCHAR DEFAULT NULL,
                experience_year VARCHAR DEFAULT NULL,
                seniority VARCHAR DEFAULT NULL,
                technology VARCHAR DEFAULT NULL,
                code_challenge_score VARCHAR DEFAULT NULL,
                technical_interview_score VARCHAR DEFAULT NULL
            )
        """)
        logging.info(f'Structure created of {self.connection_config["database"]} DB.')
