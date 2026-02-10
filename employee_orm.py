from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base, sessionmaker

#step 1
# engine=create_engine("sqlite:///company.db")
#step 2
Base = declarative_base()
'''#step 3
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department=Column(String)
#step -4
Base.metadata.create_all(engine)                             #Base.metadata → contains all table info create_all() → creates tables engine → where to create tables

#step - 5  INSERTION STEP
Session=sessionmaker(bind=engine)
session=Session()

e1=Employee(name="Nobia",age=14,department="berojgar")
e2=Employee(name="dekesuki",age=15,department="IAS")
session.add(e1)
session.add(e2)
session.commit()
#step-6
employees=session.query(Employee).all()         #session.query(Employee) → SELECT * FROM employees  .all() → fetch all rows 
for i in employees:
    print(i.id,i.name,i.age,i.department)

# employees=session.query(Employee).filter_by(id=1).first()    
# employees.name="naman"
# session.commit()
# print("employee updated")
# employees=session.query(Employee).all()
# for i in employees:
#     print(i.id,i.name,i.age,i.department)

emp = session.query(Employee).filter(Employee.id==1).first()
if emp:
    session.delete(emp)
    session.commit()
print("-----------------DELETED-------------------")

employees=session.query(Employee).all()
for i in employees:
    print(i.id,i.name,i.age,i.department)


emp = session.query(Employee).filter(Employee.age>18).all()
#LEARN ALL THE STEPS PROPERLY

#natural is rahul and age is greater than 21
AND-- emp = session.query(Employee).filter(Employee.name=="rahul",Employee.age>21).all()
oR-- emp = session.query(Employees.filter(or-(Employee.name=="rahul", employee.age>21)).all())


#******************************************************************************************************************************************************************


#ordered by
from sqlalchemy import desc, asc
emp=session.query(Employee).order_by(Employee.id).all()
print("----------------------------------------------------------------")
emp=session.query(Employee).order_by(desc(Employee.id)).limit(2).all()
'''






























from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__="departments"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    students=relationship("Student",back_populate="departments")      #back_populates = by directional relationship ko define karta hai
    students=relationship("Student",back_populates="department")      #back_populates = by directional relationship ko define karta hai

class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department_id=Column(Integer,ForeignKey("department.id"))
    department_id=Column(Integer,ForeignKey("departments.id"))
    department=relationship("Department",back_populates="students")



