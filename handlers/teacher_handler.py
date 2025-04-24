import json

def teacher_handler(handler):
    if handler.command == "GET":
        # SQL Request
        cursor = handler.db.cursor()
        sql = """
            SELECT * FROM teacher 
        """
        cursor.execute(sql)
        rows = cursor.fetchall()


        # 
        columns = [desc[0] for desc in cursor.description]
        # Список словарей
        data = [ dict(zip(columns, row)) for row in rows ]

        # Response
        handler.send_response(200)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data, default=str).encode("utf-8"))
        
    elif handler.command == "POST":
        # GET request data
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

        # GET request data
        content_length = int(handler.headers.get('Content-Length', 0))
        body = handler.rfile.read(content_length)
        data = json.loads(body)

        # 
        name = data["name"]

        # SQL
        cursor = handler.db.cursor()
        sql = """
            UPDATE teacher 
            SET name = %s
            WHERE id = %s;
        """
        # cursor.execute(sql, (handler.path_params["id"]))
        cursor.execute(sql, (name, handler.path_params["id"],))


        # Response
        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(f"CHANGED".encode("utf-8"))
        # 

    elif handler.command == "DELETE":

        # SQL
        cursor = handler.db.cursor()
        sql = """
            DELETE FROM teacher 
            WHERE id=%s;
        """
        # cursor.execute(sql, (handler.path_params["id"]))
        cursor.execute(sql, (handler.path_params["id"],))


        # Response
        handler.send_response(200)
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(f"DELETED".encode("utf-8"))
        # 