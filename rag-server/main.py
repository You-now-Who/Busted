from typing import Union
from fastapi import FastAPI
from gemini_code import generate_rag_response
from webscraper import retrieve_web_results

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/gemini_query")
def gemini_query(q: Union[str, None] = None):
    return generate_rag_response(query=q)

@app.get("/retrieve_results")
def retrieve_results(q: Union[str, None] = None):
    return retrieve_web_results(query=q)