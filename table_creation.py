from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base, sessionmaker
#step - 1
engine=create_engine("sqlite:///school.db")
#create base class
#step-2
Base= declarative_base()
#base will be parent pf all models

#step-3
class Student(Base):
    __tablename__="students"
    id=Column(Integer, primary_key=True)
    name=Column(String)
    age=Column(Integer)
    course=Column(String) 
    
#create table
Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

s1=Student(name="Rahul",age=20,course="Python") 
s2=Student(name="Karan",age=22,course="java")

session.add(s1)
session.add(s2)
session.commit()
students = session.query(Student).all()
for i in students:
    print(i.id,i.name,i.age,i.course)
print("Student added")

import os
stu=session.query(Student).filter(Student.age>20).all()
for i in stu:
    session.delete(i)
session.commit()

#natural is rahul and age is greater than 21
emp = session.query(Employee).filter(Employee.name=="rahul",Employee.age>21).all()