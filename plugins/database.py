from vars import DB_USERNAME , DB_PASSWORD , DB_NAME
from json import loads , dumps
import hashlib
import mysql.connector as mysql


def db():
    connection = mysql.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host="localhost",
        database=DB_NAME
    )


    return connection

def insert(id,data,name):
    
    links = dumps(data)
    final = links.replace("'","\\'")
    connection = db()
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO movies (id , links , name ) VALUES (%s,%s,%s)", (id,final , name.replace("'","\\'")))
    connection.commit()

    cursor.close()
    connection.close()

def update(id,res,link):
    
    # first get current resolutions 
    connection = db()
    cursor = connection.cursor()
    sql = f"SELECT * FROM movies WHERE id = '{id}' "

    cursor.execute(sql)

    results = cursor.fetchone()

    links  = loads(results[2])
    links.append({
        'res' : res,
        'link': link
    })

    linksJson = dumps(links)
    
    sql = f"UPDATE movies SET links = '{linksJson}' WHERE id = '{id}'"
    cursor.execute(sql)
    connection.commit()
    
def current_domain():    
    connection = db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM domains ORDER BY i DESC LIMIT 1')
    result = cursor.fetchone()
    return result[1]