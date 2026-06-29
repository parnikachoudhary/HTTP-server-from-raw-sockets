import socket
import threading
from request_parser import parse_http_request
from response_builder import build_response
from router import route_request
from utils import log_request


    

def handle_client(connection_door, client_addr):
    try:
        raw_bytes = connection_door.recv(1024)
        if not raw_bytes:
            return
        
        chrome_request = raw_bytes.decode('utf-8')
        print("======== CHROME REQUEST ======")
        print(chrome_request)
        print("==============================")

        method, path, version, headers, body_bytes = parse_http_request(raw_bytes)

        #===== 1. POST METHOD ============================
        if method == "POST":
            content_length = int(headers.get("content-length", 0))

            while len(body_bytes) < content_length:
                remaining = content_length - len(body_bytes)

                chunk = connection_door.recv(min(1024, remaining))

                if not chunk:
                    break

                body_bytes += chunk

        handler_function = route_request(method, path)

        if method == "GET":
            status_code, status_text, content_type, response_body_bytes = handler_function(path, body_bytes)

        else:
            status_code, status_text, content_type, response_body_bytes = handler_function(path, body_bytes)


        response = build_response(status_code, status_text, content_type, response_body_bytes)


        connection_door.send(response)

        log_request(client_addr, method, path, status_code)


    except Exception as e:
        print(f"[ERROR] Subsystem failure: {e}")
        error_content = "<h1>500 Internal Server Error</h1>"
        error_response = "HTTP\1.1 500 Internal Server Error\r\nContent-Type: text/html\r\n\r\n" + error_content
        try:
            connection_door.send(error_response.encode('utf-8'))
        except:
            pass
    #================= exception block ends =======================

    finally:
        connection_door.close()
#============== handle_client() ends ======================
def start_server():

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

if __name__ == "__main__":
    start_server()    
    