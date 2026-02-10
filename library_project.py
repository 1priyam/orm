'''
add_category() --> add books category
add_book() --> add new books
borrow_book() --> borrow a book
update_borrow() --> update borrow date
search_by_date() --> find borrowed books by date
categroy_report() --> count borrowed books per category
set_limit() --> set monthly limit 
limit_alert() --> check is limit exceeded
'''

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

#data base connection 
engine = create_engine("sqlite:///libtrack.db")
Base=declarative_base()
Session=sessionmaker(bind=engine)
session=Session()

class Category(Base):
    __tablename__= "categories"
    id=Column(Integer, primary_key=True)
    name=Column(String)
    books=relationship("Book",back_populates="category")

class Book(Base):
    __tablename="books"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    author=Column(String)
    category_id=Column(Integer,ForeignKey("categories.id"))
    Category=relationship("Category",back_populates="book")
    borrows=relationship("Borrow",back_populates="books")

class Borrow(Base):
    __tablename__="borrows"
    id=Column(Integer,primary_key=True)
    borrow_date=Column(String)
    book_id=Column(Integer,ForeignKey("books.id"))
    books=relationship("Book",back_populates="borrows")
    
class Limit(Base):
    __tablename__="limits"
    id=Column(Integer,primary_key=True)
    month=Column(String)
    max_books=Column(Integer)

def add_category():
    name=input("category name:")
    #create category object and save
    session.add(())

def add_book():
    title=input("book title:")
    author=input("author name:")
    Category_id=int(input("catgory id:"))
    #create book object
    session.add(Book(title=title,author=author,Category_id=Category_id))
    session.commit()

def borrow_book():
    book_id=int(input("Book ID:"))
    date=input("borrow date (YYY-MM-DD): ")
    #create borrow record
    session.add(Borrow(book_id=book_id,borrow_date=date))
    session.commit()
    print("book borrowed")

def update_borrow():
    bid=int(input("borrow id:"))
    #find borrrow record
    borrow=session.query(Borrow).filter(Borrow.id==bid).first()
    if borrow:
        borrow.borrow_date=input("new date:")
        session.commit()
        print("borrow updated")
    else:
        print("borrow not found")

def delete_borrow():
    bid=int(input("borrow id:"))
    borrow=session.query(Borrow).filter(Borrow.id==bid).first()
    if borrow:
        session.delete(borrow)
        session.commit()
        print("borrow deleted")
    else:
        print("borrow not found")

def search_by_date():
    date=input("enter date:")
    borrows=session.query(Borrow).filter(Borrow.borrow_date==date).all()
    for b in borrows:

