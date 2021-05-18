from http.server import BaseHTTPRequestHandler, HTTPServer
from request_handler import RequestHandler
from hotel_management import HotelManagement

request_handler: RequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        request_handler.handle(self)

    def log_message(self, format, *args):
        pass


def run(server_class=HTTPServer, handler_class=Handler):
    global request_handler
    hotel_management = HotelManagement()
    request_handler = RequestHandler()
    request_handler.link_handler('/bookRoom', hotel_management.book_room)
    this_client_address = ('', 8080)
    httpd = server_class(this_client_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
