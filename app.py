#
# Purpose: To connect to a Render PostgreSQL instance from a Flask app 
#          running on Render and set up various endpoints for the 
#          following actions in accordance with the provided steps: 
#           - Test app (hello world)
#           - Test database
#           - Create table
#           - Insert data
#           - Retrieve data and display it as an HTML table
#           - Drop table
# Author:  Noah Kawaguchi
# Usage:   Navigate to the following routes: 
#           - /
#           - /db_test 
#           - /db_create
#           - /db_insert
#           - /db_select
#           - /db_drop
#

from flask import Flask
import psycopg2


app = Flask(__name__)


# Display a simple message to confirm that the Flask app deployment is 
# working and that the app has successfully been modified from the 
# original template
@app.route('/')
def hello_world():
    return 'Hello World from Noah Kawaguchi in 3308'


# Test the database connection
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab10pg_user:ELctjWkuSDdbYUS060ld3L6nFhOnpOBx@dpg-cve20odsvqrc73f708j0-a/lab10pg")
    conn.close()
    return 'Database Connection Successful'


# Create the Basketball table
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://lab10pg_user:ELctjWkuSDdbYUS060ld3L6nFhOnpOBx@dpg-cve20odsvqrc73f708j0-a/lab10pg")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'


# Insert the provided information into the Basketball table
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://lab10pg_user:ELctjWkuSDdbYUS060ld3L6nFhOnpOBx@dpg-cve20odsvqrc73f708j0-a/lab10pg")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Populated'


# Query the Basketball table and return a formatted table of information 
# (HTML string)
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://lab10pg_user:ELctjWkuSDdbYUS060ld3L6nFhOnpOBx@dpg-cve20odsvqrc73f708j0-a/lab10pg")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string = ''
    response_string += '<table>'
    for player in records:
        response_string += '<tr>'
        for info in player:
            response_string += '<td>{}</td>'.format(info)
        response_string += '</tr>'
    response_string += '</table>'
    return response_string


# Drop the Basketball table
@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://lab10pg_user:ELctjWkuSDdbYUS060ld3L6nFhOnpOBx@dpg-cve20odsvqrc73f708j0-a/lab10pg")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Dropped'
