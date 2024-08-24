from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):

    name: str

    price: float

    is_offer: Union[bool, None] = None

#@app.get("/")
 
#async def root():

#    return {"Hello": "World"}


@app.get("/items/{item_id}")

def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")

def update_item(item_id: int, item: Item):

    return {"item_name": item.name, "item_id": item_id}


# POST method to create a new item
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price, "is_offer": item.is_offer}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with id {item_id} has been deleted."}