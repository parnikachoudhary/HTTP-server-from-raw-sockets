import socket
import os
import threading

def handle_client(connection_door, client_addr):
    try:
        raw_bytes = connection_door.recv(1024)

        chrome_request = raw_bytes.decode('utf-8')

        print("------- CHROME's REQUEST -----------")
        print(chrome_request)
        print("------------------------------------")


        request_lines = chrome_request.split('\n')
        first_line = request_lines[0]
        parts = first_line.split(' ')

        if(len(parts) >= 2):
            method = parts[0]
            path = parts[1]

            if path == "/":
                filename = "index.html"
            else:
                filename = path.lstrip("/")

            BASE_DIR = os.path.abspath(".")
            requested_abs_path = os.path.abspath(filename)

            if(os.path.commonpath([BASE_DIR]) == os.path.commonpath([BASE_DIR, requested_abs_path])):
                if os.path.exists(filename):
                    with open(filename, "r") as file:
                        content = file.read()
                    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + content  

                else:
                    not_found_error = "<h1> 404 Page Not Found</h1>"
                    response = "HTTP/1.1 404 OK\r\nContent-Type: text/html\r\n\r\n" + not_found_error

            else:
                print(f"[SECURITY ALERT] Path traversal blocked from {client_addr}")
                forbidden_content = "<h1>403 Forbidden</h1><p>Access Denied!</p>"
                response = "HTTP/1.1 403 Forbidden\r\nContent-Type: text/html\r\n\r\n" + forbidden_content


            connection_door.send(response.encode('utf-8'))

    except Exception as e:
        print(f"[ERROR] Subsystem failure: {e}")
        error_content = "<h1>500 Internal Server Error</h1>"
        error_response = "HTTP\1.1 500 Internal Server Error\r\nContent-Type: text/html\r\n\r\n" + error_content
        try:
            connection_door.send(error_response.encode('utf-8'))
        except:
            pass

    finally:
        connection_door.close()

server_door = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_door.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_door.bind(('127.0.0.1', 8080))

server_door.listen(5)

print("====================================================")
print("     CUSTOM MULTI-THREADED HTTP SERVER    ")
print("  Running on: http://127.0.0.1:8080                 ")
print("====================================================")


while(True):

    connection_door, client_addr = server_door.accept()
    print(f"\n[ALERT] A new client is connected: {client_addr}")

    new_worker = threading.Thread(target=handle_client, args=(connection_door, client_addr))

    new_worker.start()       
    