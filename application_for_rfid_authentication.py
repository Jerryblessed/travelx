

# new
#!/usr/bin/env python3

"""
    Author: donsky
    For: www.donskytech.com
    Purpose: Create a REST Server Interface using Bottle for future IOT Projects
"""



 
from bottle import route, run, request, get, response, default_app
from paste import httpserver
import sqlite3
import json
from pathlib import Path
 
# NOTE: CHANGE THIS TO WHERE YOU DOWNLOAD YOUR GIT REPO
db_folder = Path("C:/Users/opeje/OneDrive/المستندات/travelx/travelx/database.sqlite")
 
application = default_app()
 
@get('/student/isauthorized')
def message():
 
    notes = request.query.notes.lstrip().rstrip()
    length = len(notes)
    print(f"Received the following query parameter notes={notes}, len={length}")
 
    conn = sqlite3.connect(db_folder)
    cursor = conn.cursor()
 
    cursor.execute("SELECT COUNT(*) FROM ORDERS WHERE notes=?", (notes,))
    result = cursor.fetchone()
    row_count = result[0]
    print(f"query result :: ", row_count);
    cursor.close()
 
    #Set Response Header to JSON
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
 
    if(row_count > 0):
        message_result = {"is_authorized" : "true"}
    else:
        message_result = {"is_authorized": "false"}
    print(f"message_result :: {message_result}")
    return json.dumps(message_result)
 
httpserver.serve(application, host='0.0.0.0', port=8080)
# to check http://127.0.0.1:8080/student/isauthorized?notes=00-55-78 