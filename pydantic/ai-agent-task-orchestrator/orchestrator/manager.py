import uuid
from models.agent import Agent
from models.task import Task
from models.result import Result
from models.agentstate import AgentState
from models.task import TaskStatus
from datetime import datetime
class Manager:
    def __init__(self):
        self.agents: dict[uuid.UUID, Agent] = {}
        self.tasks: dict[uuid.UUID, Task] = {}
        self.results: dict[uuid.UUID, Result] = {}
        self.agent_states: dict[uuid.UUID, AgentState] = {}

    def create_agent(self,agent:Agent):
        if agent.agent_id in self.agents:
            raise ValueError("Agent already exists")
        
        self.agents[agent.agent_id] = agent
        state = AgentState(agent=agent,current_tasks=[],completed_tasks=[],active=True)
        self.agent_states[agent.agent_id]=state

    def get_agent(self,agent_id:uuid.UUID)->Agent:
        if agent_id not in self.agents:
            raise ValueError("Agent not found")
        
        return self.agents[agent_id]

    def create_task(self,task:Task):
        if task.task_id in self.tasks:
            raise ValueError("Task already exists")

        self.tasks[task.task_id]=task 

    def assign_task(self,task:Task,agent:Agent):
        if task.task_id not in self.tasks:
            raise ValueError("Task not found")
        
        if agent.agent_id not in self.agents:
            raise ValueError("Agent not found")
        
        state = self.agent_states[agent.agent_id]

        if task in state.current_tasks:
            raise ValueError("Task is already assigned to this agent")
        
        if len(state.current_tasks)>=agent.max_tasks:
            raise ValueError("Agent has reached its maximum task capacity")
            
        state.current_tasks.append(task)
        
        task.status=TaskStatus.RUNNING
        state.last_active = datetime.now()

    def complete_task(self,task: Task,agent: Agent,output: str,execution_time: float):

        if task.task_id not in self.tasks:
            raise ValueError("Task not found")

        if agent.agent_id not in self.agents:
            raise ValueError("Agent not found")

        state = self.agent_states[agent.agent_id]

        if task not in state.current_tasks:
            raise ValueError("Task is not assigned to this agent")

        state.current_tasks.remove(task)
        state.completed_tasks.append(task)

        task.status = TaskStatus.COMPLETED

        result = Result(task=task,agent=agent,output=output,success=True,execution_time=execution_time)

        self.results[result.result_id] = result
        state.last_active = datetime.now()

        return result

    def get_task(self,task_id):
        if task_id not in self.tasks:
            raise ValueError("Task not found")

        return self.tasks[task_id]
    
    def get_result(self,result_id):
        if result_id not in self.results:
            raise ValueError("Result not found")

        return self.results[result_id]
    
    def get_agent_state(self,agent_id):
        if agent_id not in self.agent_states:
            raise ValueError("Agent state not found")

        return self.agent_states[agent_id]

