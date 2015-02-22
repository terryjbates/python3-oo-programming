from wsgiref.simple_server import make_server
from io import StringIO

def message_wall_app(environ, start_response):
    output = StringIO()
    status = b'200 OK' # HTTP Status
    headers = [(b'Content-type', b'text/html; charset=utf-8')]
    start_response(status, headers)
    print("<h1>Message Wall</h1>",file=output)
    if environ['REQUEST_METHOD'] == 'POST': 
        size = int(environ['CONTENT_LENGTH'])
        post_str = environ['wsgi.input'].read(size)
        print(post_str,"<p>", file=output)
    print('<form method="POST">User: <input type="text" '
          'name="user">Message: <input type="text" '
          'name="message"><input type="submit" value="Send"></form>', 
           file=output)         
    # The returned object is going to be printed
    return [output.getvalue()]     

httpd = make_server('', 8000, message_wall_app)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()

