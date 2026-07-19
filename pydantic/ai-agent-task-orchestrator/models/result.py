from pydantic import BaseModel
import uuid
from pydantic import Field
from task import Task
from agent import Agent
from datetime import datetime

class Result(BaseModel):
    result_id : uuid.UUID = Field(default_factory=uuid.uuid4)
    task : Task
    agent : Agent
    output : str
    success : bool
    execution_time : float =Field(ge=0)
    completed_at : datetime = Field(default_factory=datetime.now)
