import json

def discipline_handler(handler):
    if handler.command == "GET":
        # SQL Request
        cursor = handler.db.cursor()
        sql = """
            SELECT * FROM discipline 
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
        # GET DATA
        content_length = int(handler.headers.get('Content-Length', 0))
        body = handler.rfile.read(content_length)
        data = json.loads(body)

        # 
        # id = data["id"]
        teacher_id = data["teacher_id"]
        name = data["name"]
        assessment_type = data["assessment_type"]
        description = data["description"]
        has_course_work = data["has_course_work"]

        # 

        # SQL Request
        cursor = handler.db.cursor()
        sql = """
            INSERT INTO discipline (teacher_id, name, assessment_type, description, has_course_work)
            VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(sql, (teacher_id, name, assessment_type, description, has_course_work))
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

        # SQL
        cursor = handler.db.cursor()
        sql = """
            DELETE FROM discipline 
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