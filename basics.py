'''ORM (Object–Relational Mapping) is a technique that lets you interact with a database
using objects instead of SQL queries.'''
#import create_engine to connect the database
from sqlalchemy import create_engine
engine=create_engine("sqlite:////school.db")
#sql lite database
#file name is school.db
#will be created if not exist
print("database connected")



'''sqlalchemy → main ORM library

create_engine → creates a connection between Python and database'''