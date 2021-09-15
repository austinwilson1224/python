import sqlite3  
import os 

ROOT = os.path.dirname(os.path.realpath(__file__))


def create_post(name, content):
    con = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values (?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts