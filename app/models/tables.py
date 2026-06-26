
# fastapi ->ORM(Object relational mapping) Sqlachemy->  database(store) 

# fastapi -> create engine -> ORM(translate python code to sql) -> psycopg2 Driver
# (send SQL to MySQL) 

# update in the database -> session.commit() -> commit the changes to the database
from sqlalchemy import Column, ForeignKey, Integer, String
from app.models.dataConfig import Base, get_db

# role base access control -> user role -> admin,student,teacher 
# 1- admin
# 2 - student
# 3 - teacher

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
