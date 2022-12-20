import os
from typing import Union

import requests
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/supplement/{item_id}")
async def get_supplement(item_id: str, q: Union[str, None] = None):
    """
    @docs:https://dsld.od.nih.gov/api-guide
    """
    respone = requests.get(
        f"https://api.ods.od.nih.gov/dsld/v8/label/{item_id}",
        timeout=10,
    )
    return respone.json()


@app.get("/food/{item_id}")
async def get_food(item_id: str, q: Union[str, None] = None):
    """
    @docs:https://fdc.nal.usda.gov/api-guide.html
    """
    respone = requests.get(
        f"https://api.nal.usda.gov/fdc/v1/food/{item_id}?api_key=DEMO_KEY",
        timeout=10,
    )
    return respone.json()
