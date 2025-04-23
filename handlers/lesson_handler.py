def lesson_handler(handler):
    if handler.command == "GET":
        # id = handler.path_params.get("id")
        # print(handler.path_params.get("id"))

        # if(id == 1):
        handler.send_response(200)
        # print("lol")
        handler.send_header("Content-type", "text/html")
        handler.end_headers()
        handler.wfile.write(f"<html><body><h1>Lesson</h1></body></html>".encode("utf-8"))

    elif handler.command == "POST":
        cursor = handler.db.cursor()
        query = 'INSERT INTO test VALUES(%s, %s);'
        cursor.execute(query, ('vadim', 10))

    elif handler.command == "PUT":
        ...
    elif handler.command == "DELETE":
        ...