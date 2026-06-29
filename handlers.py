import os
from mime_types import get_content_type
from utils import is_safe_path

def handle_static_file(path, body_bytes):
    if path == "/":
        filename = "index.html"
    else:
        filename = path.lstrip("/")
    
    safe_file_path = os.path.join("www", filename)

    if not is_safe_path("www", safe_file_path):
        return 403, "Forbidden", "text/html", b"<h1>403 Forbidden</h1><p>Access Denied!</p>"
    
    if os.path.exists(safe_file_path):
        with open (safe_file_path, "rb") as file:
            file_content = file.read ()

            _, extension = os.path.splitext(filename)

            content_type = get_content_type(extension)

            return 200, "OK", content_type, file_content
        
    else:
        return 404, "Not Found", "text/html", b"<h1>404 Page Not Found</h1>"
    
def handle_api_echo(path, body_bytes):
    user_data = body_bytes.decode('utf-8', errors='ignore')
    response_body = '{"status": "success", "echoed_data": "' + user_data + '"}'

    return 200, "OK", "application/json", response_body.encode('utf-8')