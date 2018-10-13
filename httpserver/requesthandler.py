from http.server import BaseHTTPRequestHandler
from lib.utils.json import dict_to_json, json_to_dict
import lib.consts.errors as errors

class RequestHandler(BaseHTTPRequestHandler):
    """TODO: write comments

    """
    def __init__(self, request, client_address, server):
        self.__request = request
        self.__response_headers = {
            'Content-type': 'application/json'
        }
        self.__response_body = {
            'data': 'POST response: response_body not altered',
            'error': errors.RESPONSE_BODY_NOT_ALTERED
        }
        self.__client_address = client_address
        self.__response_code = 500
        super().__init__(request, client_address, server)

    @property
    def client_address(self):
        return self.__client_address

    @client_address.setter
    def client_address(self, value):
        self.__client_address = value

    @property
    def request(self):
        return self.__request

    @request.setter
    def request(self, value):
        self.__request = value

    @property
    def response_code(self):
        return self.__response_code

    @response_code.setter
    def response_code(self, value):
        self.__response_code = value

    @property
    def response_headers(self):
        return self.__response_headers

    @response_headers.setter
    def response_headers(self, value):
        self.__response_headers = value

    @property
    def response_body(self):
        return self.__response_body

    @response_body.setter
    def response_body(self, value):
        self.__response_body = value

    def get_request_params(self):
        length = int(self.headers.get('content-length', 0))
        params = self.rfile.read(length)
        params = json_to_dict(params)
        return params

    def do_POST(self):
        self.__response_code = 200
        super(RequestHandler, self).send_response(self.__response_code)
        for k, v in self.__response_headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(dict_to_json(self.__response_body).encode())

    def do_GET(self):
        super(RequestHandler, self).send_response(200)
        for k, v in self.__response_headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.__response_body = {
            'data': 'HTTP method not supported by service',
            'error': errors.HTTP_METHOD_NOT_SUPPORTED
        }
        self.wfile.write(dict_to_json(self.__response_body).encode())
