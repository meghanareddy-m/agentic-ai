from enum import Enum
from pydantic import BaseModel
from pydantic import Field
from datetime import datetime
import uuid
from pydantic import field_validator

class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PAUSED = "PAUSED"

class TaskPriority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Task(BaseModel):
    task_id : uuid.UUID = Field(default_factory=uuid.uuid4)
    title : str = Field(...,min_length=1,max_length=100)
    description  : str | None = None
    priority : TaskPriority = TaskPriority.MEDIUM
    status : TaskStatus = TaskStatus.PENDING
    created_at : datetime = Field(default_factory=datetime.now)

    @field_validator("title")
    @classmethod
    def validate_title(cls,value):
        cleaned = value.strip()
        if not cleaned:
            raise ValueError
        
        return cleaned