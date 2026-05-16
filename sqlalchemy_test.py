from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection
engine = create_engine("sqlite:///school_db.db")

# Base class
Base = declarative_base()

# Table class
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email=Column(String(100))
   
# Create table in SQLite
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Descending data
student=session.query(Student).order_by(Student.age.desc()).all()
session.commit()


print("Data inserted successfully")