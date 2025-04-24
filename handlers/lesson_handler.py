import json

def lesson_handler(handler):
    if handler.command == "GET":
        ...
        # id = handler.path_params.get("id")
        # print(handler.path_params.get("id"))

        # if(id == 1):
        # handler.send_response(200)
        # # print("lol")
        # handler.send_header("Content-type", "text/html")
        # handler.end_headers()
        # handler.wfile.write(f"<html><body><h1>Lesson</h1></body></html>".encode("utf-8"))

    elif handler.command == "POST":
        content_length = int(handler.headers.get('Content-Length', 0))
        body = handler.rfile.read(content_length)
        data = json.loads(body)

        id = data["id"]
        discipline_id = data["discipline_id"]
        lesson_type = data["lesson_type"]
        name = data["name"]

        cursor = handler.db.cursor()
        sql = """
            INSERT INTO lesson (id, discipline_id, lesson_type, name)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(sql, (id, discipline_id, lesson_type, name))
        handler.db.commit()


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