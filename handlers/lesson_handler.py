import json

def lesson_handler(handler):
    if handler.command == "GET":
        # SQL Request
        cursor = handler.db.cursor()
        sql = """
            SELECT * FROM lesson 
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
        handler.send_header("Access-Control-Allow-Origin", "*")
        handler.end_headers()
        handler.wfile.write(json.dumps(data, default=str).encode("utf-8"))

    elif handler.command == "POST":
        content_length = int(handler.headers.get('Content-Length', 0))
        body = handler.rfile.read(content_length)
        data = json.loads(body)

        # id = data["id"]
        discipline_id = data["discipline_id"]
        lesson_type = data["lesson_type"]
        name = data["name"]

        cursor = handler.db.cursor()
        sql = """
            INSERT INTO lesson (discipline_id, lesson_type, name)
            VALUES (%s, %s, %s);
        """
        cursor.execute(sql, (discipline_id, lesson_type, name))
        handler.db.commit()


        # Response
        handler.send_response(200)
        handler.send_header("Content-type", "text/html", 'Access-Control-Allow-Origin')
        handler.end_headers()
        handler.wfile.write(f"HI".encode("utf-8"))
        # 

    elif handler.command == "PUT":
        ...
    elif handler.command == "DELETE":

        # SQL
        cursor = handler.db.cursor()
        sql = """
            DELETE FROM lesson 
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