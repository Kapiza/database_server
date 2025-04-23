from http.server import BaseHTTPRequestHandler
from handlers.lesson_handler import lesson_handler
from handlers.discipline_handler import discipline_handler
from handlers.teacher_handler import teacher_handler

from urllib.parse import urlparse


routes = {
    "lesson": lesson_handler,
    "discipline": discipline_handler, 
    "teacher": teacher_handler
}

def make_handler_class(db_conn):
    class PostgresApiServer(BaseHTTPRequestHandler):
        def setup(self): # how does it work?
              super().setup()
              self.db = db_conn

        def do_GET(self): 
                parsed_path = urlparse(self.path)
                path_parts = parsed_path.path.strip("/").split("/")  # ["lesson", "5"]      

                handler = routes.get(path_parts[0])        
                handler(self)
        def do_POST(self): 
                parsed_path = urlparse(self.path)
                path_parts = parsed_path.path.strip("/").split("/")  # ["lesson", "5"]      

                handler = routes.get(path_parts[0])        
                handler(self)
        def do_PUT(self):
                parsed_path = urlparse(self.path)
                path_parts = parsed_path.path.strip("/").split("/")  # ["lesson", "5"]      

                if len(path_parts) == 2:
                    self.path_params = {"id": int(path_parts[1])}
                    handler = routes.get(path_parts[0])        
                    handler(self)        
        def do_DELETE(self): 
                parsed_path = urlparse(self.path)
                path_parts = parsed_path.path.strip("/").split("/")  # ["lesson", "5"]      
                if len(path_parts) == 2:
                    self.path_params = {"id": int(path_parts[1])}
                    handler = routes.get(path_parts[0])        
                    handler(self)      
    return PostgresApiServer






            # def __init__(self, conn, *args, **kwargs):  # Initialise server with database connection
            #     self.db = db_conn  
                # ...
                # super().__init__(*args, **kwargs)  # понятия не имею нахрена это

                # cursor = self.db.cursor()







                # if len(path_parts) == 2:
                #     lesson_handler(self)
                # handler = routes.get(self.path)
                # if handler:
                #     handler(self)