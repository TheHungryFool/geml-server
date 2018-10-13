from http.server import HTTPServer as Server
from .requesthandler import RequestHandler

class HTTPServer():
    def __init__(self):
        self.__port = 6969
        self.__host = ''
        self.__handler = RequestHandler
        self.__message = 'Warming up...'
        self.__server = False

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    def start(self):
        try:
            self.__server = Server((self.__host, self.__port), self.__handler)
            print(self.__message)
            print('Starting HTTP server @ {}:{}'
                  .format('localhost' if not self.__host else self.host, self.__port))

            # keep till a KeyboardInterrupt (^c) is observed
            self.__server.serve_forever()

        except KeyboardInterrupt:
            print('\nShutting down the server (^C pressed)')
            self.__server.socket.close()

        except Exception as e:
            if e.errno == 98:
                # if the port is already in use, use a different port
                # (normal when multiple server instances are run)
                self.__port = (self.__port + 50) % 10000
                self.start()

            # something has actually gone wrong
            print('Oops! Something went wrong')

    def stop(self):
        self.__server.socket.close()
