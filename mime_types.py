MIME_MAPPING = {
    ".html": "text/html",
    ".css": "text/css",
    ".js": "application/javascript",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg"
}

def get_content_type(extension):
    return MIME_MAPPING.get(extension, "text/plain")