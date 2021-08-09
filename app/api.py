import os

from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI, Body
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import spacy
import srsly

from app.models import (
    POSMultipleRequest,
    POSMultipleResponse
)

from app.spacy_pos import SpacyPOS


load_dotenv(find_dotenv())
prefix = os.getenv("CLUSTER_ROUTE_PREFIX", "").rstrip("/")


# create app
app = FastAPI(
    title="POS",
    version="1.0",
    description="A simple API that takes a body of text and returns grammatical information.",
    openapi_prefix=prefix,
)

origins = [

    "http://localhost",
    "http://localhost:3000",
    "http://143.198.98.65:3000/",
    "http://143.198.98.65"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load example request for docs
example_request = srsly.read_json("app/data/example_request.json")

# load spacy models
nlp_en = spacy.load("en_core_web_sm")
# TODO: include more languages

# create a POS parser with English model
pos_parser = SpacyPOS(nlp_en)


# redirect index to docs
@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"{prefix}/docs")


# api route to get POS data
@app.post("/pos", tags=["POS Tagging"], response_model=POSMultipleResponse)
async def extract_pos(body: POSMultipleRequest = Body(..., example=example_request)):
    documents = []

    # format request into a series of documents that can be passed to our parser
    for val in body.values:
        documents.append({"id": val.recordId, "text": val.data.text})

    # parse the data to get POS info
    pos_res = pos_parser.extract_pos(documents)

    # format response properly
    res = {"values": [{"recordId": k, "data": d} for k, d in pos_res.items()]}

    return res
