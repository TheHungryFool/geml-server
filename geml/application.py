from httpserver.server import HTTPServer

class geml(HTTPServer):
    def __init__(self):
        super().__init__()

    def start(self, host=False, port=False):
        if host:
            self.__host = host
        if port:
            self.__port = port

        # start the HTTP server
        super().start()
