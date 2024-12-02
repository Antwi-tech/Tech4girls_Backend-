# This file is simply created to establish a connection between the databse created and python by using 
# sqlalchemy
# The sessionmaker jsut creates an interface to interact with the databse. It has functionalities like
# add, query.filter_by,commit and other methods for interactivity

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


database_username = os.getenv("DB_USERNAME")
database_password = os.getenv("DB_PASSWORD")
database_name = os.getenv('DB_NAME')

# This string is used to specify the path to the exact database on your machine.
connection_str = f'mysql+mysqlconnector://{database_username}:{database_password}@localhost/{database_name}'

# Since sql create_engine is used to extablish the connection, the variable connection_str is passed to it
# to ensure that that the database specified is used 
engine = create_engine(connection_str)

# This is to test if the connection has been established successfully
try:
    connection = engine.connect()
    print('Connection established successfully')
    connection.close()
    
except Exception as e:
    print(f'An error occured: {e}')    
    
    
# This ensures that any session creates will be bound to the engine that holds the data you want to manipulate
DBSession = sessionmaker(bind=engine)
# This is simply creating an instance of session to be able to use it's objects 
session =   DBSession()