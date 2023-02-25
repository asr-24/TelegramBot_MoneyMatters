from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text


# Define the database engine and session
engine = create_engine('sqlite:///moneyMatters.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the data model using a declarative base class
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key = True)
    userid = Column(Integer, nullable = False)
    password = Column(Integer, nullable = False)
    first_name = Column(Integer, nullable = False)
    last_name =  Column(String)
    chat_type = Column(String, nullable = True)
    group_chat_created = Column(String, nullable = False)
    is_bot = Column(String, nullable = False)


# Create the table in the database
Base.metadata.create_all(engine)

# Insert data into the database
user = User(username = 'trial7', 
            userid = 2222, 
            password = 'blahblahdilmil', 
            first_name = 'HHHH', 
            last_name = 'Mishra', 
            chat_type = 'nahiPata',
            group_chat_created = 'noKnow',
            is_bot = 'no')

try:
    # session.add(user)
    # session.commit()
    print("sure")
finally:
    print("done")

# customers = [
#     Customer(name='Jane Doe', email='jane.doe@example.com', age=28),
#     Customer(name='Bob Johnson', email='bob.johnson@example.com', age=42)
# ]
# session.add_all(customers)
# session.commit()

# Select all users
result = engine.execute("SELECT * FROM users")
#result = engine.execute("DELETE FROM users")

rows = result.fetchall()

if len(rows) == 0:
    print("bhag")
else:
    for row in rows:
        print(row)
