from handlers import handle_static_file, handle_api_echo

def route_request(method, path):

    if method == "POST" and path == "/api/echo":
        return handle_api_echo
        
    elif method == "GET":
        return handle_static_file
    
    return None