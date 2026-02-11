============================================= PROBLEM STATEMENT =================================================

FINTRACK PRO – CLI FINANCE MANAGER Project Documentation

Introduction FinTrack Pro is a command line based personal finance management system developed using Python, SQLite and SQLAlchemy ORM. The project helps users to manage daily expenses, track subscriptions, search records, maintain monthly budgets and generate analytics using raw SQL queries.

Objectives • To understand ORM based database interaction
• To use SQLite with Python
• To implement CRUD operations
• To write raw SQL for analytics
• To design modular architecture
• To build interview oriented project

Technologies Used • Python
• SQLite Database
• SQLAlchemy ORM
• Raw SQL Queries
• CLI Interface

System Features • Add Expense
• Update Expense
• Delete Expense
• Search by Date
• Category Analytics
• Monthly Budget Alert
• Persistent Storage

Database Design

Tables:

categories(id, name)
expenses(id, title, amount, date, category_id)
subscriptions(id, name, amount, next_date)
budgets(id, month, limit)
Relationships: Category 1 ---- N Expenses

Modules Description
a) Expense Module

Add new expense
Update existing expense
Delete expense
ORM based operations
b) Report Module

Category wise total
Aggregation using GROUP BY
Raw SQL joins
c) Budget Module

Set monthly limit
Compare with spending
Alert when exceeded
d) Search Module

Find expenses by date using SQL query
Sample SQL Used
SELECT c.name, SUM(e.amount) FROM categories c JOIN expenses e ON c.id = e.category_id GROUP BY c.name;

Learning Outcomes • ORM concepts
• SQL joins & aggregation
• Modular programming
• Exception handling
• CLI application design

Future Enhancements • CSV Export
• Flask UI
• Authentication
• Charts integration

Conclusion This project demonstrates practical use of Python with databases and SQL. It is suitable for resume showcase and interview explanation.

💰 FINTRACK PRO – CLI Finance Manager

FinTrack Pro is a command-line based personal finance management system developed using Python, SQLite, and SQLAlchemy ORM. The project helps users record daily expenses, organize spending by category, monitor monthly budgets, and generate analytical reports using both ORM-based queries and raw SQL. It is designed as a learning-focused yet practical project, suitable for academic evaluation, interviews, and resume showcase.

📌 Features

Add, update, and delete expenses

Create and manage expense categories

Search expenses by date

Generate category-wise spending reports

Set monthly budget limits

Get alerts when budget limits are exceeded

Persistent data storage using SQLite

Menu-driven CLI interface

🎯 Project Objectives

Understand ORM-based database interaction

Work with SQLite database using Python

Implement full CRUD operations

Combine SQLAlchemy ORM with raw SQL queries

Design a modular and maintainable CLI application

Build an interview-oriented real-world project

🛠 Technologies Used

Python

SQLite Database

SQLAlchemy ORM

Raw SQL Queries

Command Line Interface (CLI)

🗂 Project Structure fintrack_pro/ │ ├── fintrack.py # Main application file ├── fintrack.db # SQLite database (auto-generated) ├── README.md # Project documentation

🧱 Database Design Tables

categories

id (Primary Key)

name (Unique)

expenses

id (Primary Key)

title

amount

date

category_id (Foreign Key)

budgets

id (Primary Key)

month (Unique – YYYY-MM)

limit

Relationships

One-to-Many Relationship

One Category can have multiple Expenses

⚙️ How the Code Works Database Connection

SQLAlchemy engine connects Python to the SQLite database

declarative_base() is used to define ORM models

sessionmaker() manages database sessions for queries and transactions

ORM Models

Category Model stores expense categories and maintains relationship with expenses

Expense Model stores individual expense records linked to categories

Budget Model stores monthly spending limits

CRUD Operations

Create: Add new categories, expenses, and budgets

Read: Search expenses and generate reports

Update: Modify existing expenses

Delete: Remove expense records

Reports & Analytics

Uses raw SQL queries for aggregation and reporting

Demonstrates JOIN, GROUP BY, and SUM operations

Example:

SELECT c.name, SUM(e.amount) FROM categories c JOIN expenses e ON c.id = e.category_id GROUP BY c.name;

Budget Monitoring

Monthly expenses are calculated using SQL

Compared against stored budget limits

Displays alerts when spending exceeds the limit

🖥 CLI Menu Options

Add category
Add expense
Update expense
Delete expense
Search by date
Category report
Set monthly budget
Budget alert
Exit
🚀 How to Run the Project Prerequisites

Python 3.x installed

Install Required Package pip install sqlalchemy

Run the Application python fintrack.py

📚 Learning Outcomes

Practical understanding of SQLAlchemy ORM

Experience with database relationships

Writing raw SQL within Python applications

Designing menu-driven CLI systems

Applying modular programming principles

Handling real-world finance-related data

🔮 Future Enhancements

Export reports to CSV

Web interface using Flask

User authentication

Graphical charts and dashboards

Cloud database integration

🧠 Why This Project Matters

FinTrack Pro demonstrates the ability to:

Design and manage databases

Implement real-world business logic

Write clean, readable, and modular Python code

Combine ORM and SQL effectively This makes it an excellent project for academic submissions, interviews, and professional portfolios.
