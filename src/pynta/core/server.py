from wsgiref.simple_server import make_server


def serve(host, port, app):
    server = make_server(host, port, app)
    server.serve_forever()
