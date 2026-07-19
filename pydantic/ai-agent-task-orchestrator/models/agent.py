from enum import Enum
from pydantic import BaseModel
from pydantic import Field
import uuid
from pydantic import field_validator

class AgentRole(Enum):
    RESEARCH="RESEARCH"
    CODING="CODING"
    WRITING="WRITING"
    REVIEW="REVIEW"

class Agent(BaseModel):
    agent_id:uuid.UUID=Field(default_factory=uuid.uuid4)
    name :str=Field(...,min_length=1,max_length=50)
    role : AgentRole
    skills : list[str]
    max_tasks : int = Field(default=5,ge=1,le=5)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        cleaned = value.strip()
        if not cleaned:
            raise ValueError
        
        return cleaned
    
    @field_validator("skills")
    @classmethod
    def validate_skills(cls,value):
        if not value:
            raise ValueError("Skills cannot be empty")
        
        for s in value:
            cleaned = s.strip()
            if not cleaned:
                raise ValueError("Skills cannot be empty")
        
        if ((len(value)) != len(set(value))):
            raise ValueError("Duplicate skills are not allowed")
        
        cleaned_skills=[]
        for s in value:
            cleaned = s.strip()
            cleaned_skills.append(cleaned)

        return cleaned_skills

