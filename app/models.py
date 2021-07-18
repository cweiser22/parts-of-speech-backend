from typing import List, Optional
from pydantic import BaseModel


class POSDataRequest(BaseModel):
    text: str
    language: str = "en"


class POSRequest(BaseModel):
    recordId: str
    data: POSDataRequest


class POSMultipleRequest(BaseModel):
    values: List[POSRequest]


class POSResponseData(BaseModel):
    adjectives: List
    adverbs: List
    interjections: List
    verbs: List
    pronouns: List
    articles: List
    prepositions: List
    conjunctions: List
    nouns: List


class Message(BaseModel):
    message: str


class POSResponse(BaseModel):
    recordId: str
    data: POSResponseData
    errors: Optional[List[Message]]
    warnings: Optional[List[Message]]


class POSMultipleResponse(BaseModel):
    values: List[POSResponse]


