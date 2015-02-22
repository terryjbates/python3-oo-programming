from wsgiref.simple_server import make_server

def message_wall_app(environ, start_response):
    status = b'200 OK' # HTTP Status
    headers = [(b'Content-type', b'text/html; charset=utf-8')]       
    start_response(status, headers)

    # The returned object is going to be printed
    return ["<h1>Message Wall</h1>"]

httpd = make_server('', 8000, message_wall_app)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()

