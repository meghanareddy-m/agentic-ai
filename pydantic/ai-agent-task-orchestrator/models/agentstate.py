from pydantic import BaseModel
from models.task import Task
from datetime import datetime
from pydantic import Field
from models.agent import Agent
from pydantic import computed_field

class AgentState(BaseModel):
    agent : Agent
    current_tasks : list[Task] = Field(default_factory=list)
    completed_tasks : list[Task] = Field(default_factory=list)
    active : bool
    last_active : datetime=Field(default_factory=datetime.now)

    @computed_field
    @property
    def total_completed_tasks(self) -> int:
        return(len(self.completed_tasks))
