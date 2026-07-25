from pydantic import BaseModel
from pydantic import Field
from datetime import datetime
from pydantic import field_validator
from pydantic import HttpUrl
from typing import Literal

class ResearchResult(BaseModel):
    title : str = Field(...,min_length=1,max_length=300)
    url : HttpUrl
    source : Literal["GitHub","HackerNews"]

    @field_validator("title")
    @classmethod
    def validate_title(cls,value:str)->str:
        cleaned=value.strip()
        if not cleaned:
            raise ValueError("Title can't be empty")

        return cleaned
        
class ResearchSession(BaseModel):
    topic : str = Field(...,min_length=1,max_length=100)
    timestamp : datetime = Field(default_factory=datetime.now)
    results : list[ResearchResult] =Field(...,min_length=1)

    @field_validator("topic")
    @classmethod
    def validate_topic(cls,value:str)->str:
        cleaned=value.strip()
        if not cleaned:
            raise ValueError("Topic can't be empty")

        return cleaned


