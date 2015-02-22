from wsgiref.simple_server import make_server
from io import StringIO
from urllib.parse import unquote_plus
import sqlite3
import datetime

def get_form_vals(post_str):
    form_vals = {item.split("=")[0]:item.split("=")[1] for item \
                 in post_str.split("&")}
    return form_vals

def message_table(messages):
    table = "<table>\n"
    for message in messages:
        row_str = "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>\n"
        table += row_str.format(message[2], message[0], message[1])
    table += "</table>"
    return table

def message_wall_app(environ, start_response):
    output = StringIO()
    status = b'200 OK' # HTTP Status
    headers = [(b'Content-type', b'text/html; charset=utf-8')]
    start_response(status, headers)
    print("<h1>Message Wall</h1>",file=output)
    if environ['REQUEST_METHOD'] == 'POST':
       size = int(environ['CONTENT_LENGTH'])
       post_str = environ['wsgi.input'].read(size)
       post_str = unquote_plus(post_str.decode())
       form_vals = get_form_vals(post_str)
       form_vals['timestamp'] = datetime.datetime.now()
       cursor.execute("""insert into messages (user, message, ts) values 
                      (:user,:message,:timestamp)""", form_vals) 
    path_vals = environ['PATH_INFO'][1:].split("/")                   #B
    user,*tag = path_vals
    cursor.execute("""select * from messages where user like ? or message 
                    like ? order by ts""", (user,"@"+user+"%"))       #C
    print(message_table(cursor.fetchall()), "<p>", file=output)  
                 
    
    print('<form method="POST">User: <input type="text" '
          'name="user">Message: <input type="text" '
          'name="message"><input type="submit" value="Send"></form>', 
           file=output)
    # The returned object is going to be printed
    return [output.getvalue()]

httpd = make_server('', 8000, message_wall_app)
print("Serving on port 8000...")

conn = sqlite3.connect("messaging")
cursor = conn.cursor()
# Serve until process is killed
httpd.serve_forever()

