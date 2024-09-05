secret_key="12345"
print(secret_key)
import os

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_env_var(var_name):
    return os.getenv(var_name)
