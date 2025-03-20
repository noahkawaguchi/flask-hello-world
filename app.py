from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Noah Kawaguchi in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab10pg_user:ELctjWkuSDdbYUS060ld3L6nFhOnpOBx@dpg-cve20odsvqrc73f708j0-a/lab10pg")
    conn.close()
    return 'Database Connection Successful'

