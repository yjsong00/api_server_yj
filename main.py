from fastapi import FastAPI
from db import get_db
from crud import create_item, get_items
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.post("/items/")
async def create_item_endpoint(item: Item):
    db = get_db()
    return create_item(db, item)

@app.get("/items/")
async def get_items_endpoint():
    db = get_db()
    return get_items(db)

