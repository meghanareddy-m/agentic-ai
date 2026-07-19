import uuid

from models.agent import Agent
from models.task import Task
from models.result import Result
from models.agentstate import AgentState


class Manager:
    def __init__(self):
        self.agents: dict[uuid.UUID, Agent] = {}
        self.tasks: dict[uuid.UUID, Task] = {}
        self.results: dict[uuid.UUID, Result] = {}
        self.agent_states: dict[uuid.UUID, AgentState] = {}

