def parse_http_request(raw_bytes):
    parts = raw_bytes.split(b"\r\n\r\n", 1)
    header_bytes = parts[0]
    initial_body_bytes = parts[1] if len(parts) > 1 else b""

    header_string = header_bytes.decode('utf-8', errors='ignore')
    header_lines = header_string.split("\r\n")

    request_line_parts = header_lines[0].split(" ")
    method = request_line_parts[0]
    path = request_line_parts[1]
    version = request_line_parts[2]

    headers = {}
    for line in header_lines[1 : ]:
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()

    
    return method, path, version, headers, initial_body_bytes