from wsgiref.simple_server import make_server


def serve(host, port, app):
    server = make_server(host, port, app)
    print(('Simple server started on %s:%s.' % (host, port)))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Simple server stopped.')
