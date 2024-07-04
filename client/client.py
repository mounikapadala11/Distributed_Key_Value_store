import requests

base_url = "http://localhost:8000"

def create_key(key, value):
    response = requests.post(f"{base_url}/create/{key}", json={"value": value})
    return response.json()

def read_key(key):
    response = requests.get(f"{base_url}/read/{key}")
    return response.json()

def update_key(key, value):
    response = requests.put(f"{base_url}/update/{key}", json={"value": value})
    return response.json()

def delete_key(key):
    response = requests.delete(f"{base_url}/delete/{key}")
    return response.json()

def add_node(node):
    response = requests.post(f"{base_url}/add_node/{node}")
    return response.json()

def get_node(key):
    response = requests.get(f"{base_url}/get_node/{key}")
    return response.json()

# Example usage
print(create_key("name", "Alice"))
print(read_key("name"))
print(update_key("name", "Bob"))
print(delete_key("name"))
print(add_node("node1"))
print(get_node("name"))
