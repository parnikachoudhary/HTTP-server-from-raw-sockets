
def build_response(status_code, status_text, content_type, body_bytes):
    header_text = f"HTTP/1.1 {status_code} {status_text}\r\nContent-Type: {content_type}\r\nContent-Length: {len(body_bytes)}\r\n\r\n"

    return header_text.encode('utf-8') + body_bytes