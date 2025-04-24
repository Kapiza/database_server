import json

def teacher_handler(handler):
    if handler.command == "GET":
        # SQL Request
        cursor = handler.db.cursor()
        sql = """
            SELECT * FROM teacher 
        """
        cursor.execute(sql, (id, name))

        rows = cursor.fetchall()

        # handler.db.commit()
        # 

        # Response
        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(f"HI".encode("utf-8"))
    elif handler.command == "POST":
        # GET DATA
        content_length = int(handler.headers.get('Content-Length', 0))
        body = handler.rfile.read(content_length)
        data = json.loads(body)

        # 
        id = data["id"]
        name = data["name"]
        # 

        # SQL Request
        cursor = handler.db.cursor()
        sql = """
            INSERT INTO teacher (id, name)
            VALUES (%s, %s);
        """
        cursor.execute(sql, (id, name))
        handler.db.commit()
        # 

        # Response
        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(f"HI".encode("utf-8"))
        # 
    elif handler.command == "PUT":
        ...
    elif handler.command == "DELETE":
        ...