import os
import datetime

BASE_DIR = os.path.abspath(".")

def is_safe_path(safe_dir, file_path):
    requested_abs_path = os.path.abspath(file_path)

    base_abs_path = os.path.abspath(safe_dir)

    return base_abs_path == os.path.commonpath([base_abs_path, requested_abs_path])

def log_request(client_addr, method, path, status_code):
    timestamp = datetime.datetime.now().strftime(f"Date : %Y-%m-%d | Time : %H:%M:%S")
    print(f"[{timestamp}] {client_addr} - {method} {path} -> Status: {status_code}")