from http.server import BaseHTTPRequestHandler
from handlers.lesson_handler import lesson_handler
from handlers.discipline_handler import discipline_handler
from handlers.teacher_handler import teacher_handler


routes = {
    "/lesson": lesson_handler,
    "/discipline": discipline_handler, 
    "/teacher": teacher_handler
}

class PostgresApiServer(BaseHTTPRequestHandler):
    def __init__(self, conn, *args, **kwargs):  # Initialise server with database connection
        self.db = conn
        # super().__init__(*args, **kwargs)  # понятия не имею нахрена это

        # cursor = self.db.cursor()

    def do_GET(self): 
            handler = routes.get(self.path)
            if handler:
                handler(self)
    def do_POST(self): 
            handler = routes.get(self.path)
            if handler:
                handler(self)
    def do_DELETE(self): 
            handler = routes.get(self.path)
            if handler:
                handler(self)         
    def do_PUT(self):
            handler = routes.get(self.path)
            if handler:
                handler(self)        