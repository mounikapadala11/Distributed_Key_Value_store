from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .kv_store import KeyValueStore
from .consistent_hashing import ConsistentHashing

app = FastAPI()
kv_store = KeyValueStore()
hash_ring = ConsistentHashing()

class Item(BaseModel):
    value: str

@app.post("/create/{key}")
def create(key: str, item: Item):
    if kv_store.create(key, item.value):
        return {"message": "Created"}
    else:
        raise HTTPException(status_code=400, detail="Key already exists")

@app.get("/read/{key}")
def read(key: str):
    value = kv_store.read(key)
    if value is not None:
        return {"key": key, "value": value}
    else:
        raise HTTPException(status_code=404, detail="Key not found")

@app.put("/update/{key}")
def update(key: str, item: Item):
    if kv_store.update(key, item.value):
        return {"message": "Updated"}
    else:
        raise HTTPException(status_code=404, detail="Key not found")

@app.delete("/delete/{key}")
def delete(key: str):
    if kv_store.delete(key):
        return {"message": "Deleted"}
    else:
        raise HTTPException(status_code=404, detail="Key not found")

@app.post("/add_node/{node}")
def add_node(node: str):
    hash_ring.add_node(node)
    return {"message": f"Node {node} added to the ring"}

@app.get("/get_node/{key}")
def get_node(key: str):
    node = hash_ring.get_node(key)
    return {"key": key, "node": node}
