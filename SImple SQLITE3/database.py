import sqlite3

#Query the DB and return all records
def show_all():
    #connect to db
    conn =sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    #Query The Db
    c.execute("SELECT  rowid, * FROM customers ")
    z=c.fetchall()
    for item in z:
        print(item)
    
    #commit 
    conn.commit()
    # close our conn
    conn.close

#Query the DB and add records
def add_one(fname,lname,email):
    #connect to db
    conn =sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(fname,lname,email))
    #commit 
    conn.commit()
    # close our conn
    conn.close

def add_many(lists):
    #connect to db
    conn =sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)",(lists))
    #commit 
    conn.commit()
    # close our conn
    conn.close

def delete_one(id):
    #connect to db
    conn =sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid=(?)",id)
    #commit 
    conn.commit()
    # close our conn
    conn.close

def search_email(email):
    #connect to db
    conn =sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE email = (?)",(email, ))
    z=c.fetchall()
    for item in z:
        print(item)
    #commit 
    conn.commit()
    # close our conn
    conn.close