from enum import Enum
from dataclasses import dataclass
from pathlib import Path
import json
from dataclasses import asdict

def log_action(func):
    def wrapper(*args,**kwargs):
        print(f"Executing {func.__name__}")
        return func(*args,**kwargs)
    return wrapper


class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

@dataclass
class Task:
    id : int
    title : str
    description : str
    status : TaskStatus

@dataclass
class AgentState:
    current_task : Task | None
    task_count : int
    workspace : Path

class TaskNotFoundError(Exception):
    pass

class TaskManager:
    def __init__(self):
        self.tasks : dict[int, Task] = { }
        self.next_task_id : int = 1

    @log_action
    def create_task(self, title : str, description : str) -> Task :
        task_id = self.next_task_id
        task = Task(id=task_id,title=title,description=description,status=TaskStatus.PENDING)
        self.tasks[task_id]= task
        self.next_task_id+=1

        return task

    def get_task(self,task_id:int) -> Task:
        if task_id not in self.tasks:
            raise TaskNotFoundError(f"{task_id} not found")
    
        return self.tasks[task_id]

    def update_task(self,task_id:int,title:str | None = None, description: str | None=None) -> Task:
        task = self.get_task(task_id)

        if title is not None:
            task.title=title
        if description is not None:
            task.description=description

        return task

    def update_status(self,task_id:int,status: TaskStatus) -> Task:
        task=self.get_task(task_id)
        task.status=status

        return task

    def delete_task(self,task_id:int) -> None :
        if task_id not in self.tasks:
            raise TaskNotFoundError(f"{task_id} not found")
    
        del self.tasks[task_id]

    def list_tasks(self) -> list[Task]:
        return list(self.tasks.values())
    
    def pending_tasks(self):
        for task in self.tasks.values():
            if task.status == TaskStatus.PENDING:
                yield task

    def save_tasks(self,file_path:Path) -> None:
        data = []
        for task in self.tasks.values():
            task_dict=asdict(task)
            task_dict["status"]= task.status.value
            data.append(task_dict)

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_tasks(self,file_path:Path) -> None:

        if not file_path.exists():
            return

        with open(file_path, "r") as file:
            data=json.load(file)

        self.tasks.clear()
        for item in data:
            task=Task(id=item["id"],title=item["title"],description=item["description"],status=TaskStatus(item["status"]))
            self.tasks[task.id] = task

        if self.tasks:
            self.next_task_id=max(self.tasks.keys()) + 1
        else:
            self.next_task_id=1


workspace=Path("workspace")
tasks_dir=workspace/ "tasks"
logs_dir=workspace/ "logs"
tasks_dir.mkdir(parents=True,exist_ok=True)
logs_dir.mkdir(parents=True,exist_ok=True)


if __name__ == "__main__" :

    manager = TaskManager()

    task1= manager.create_task("Learn Python Fundamentals","Study OOP and other core components")

    task2= manager.create_task("Build an agent","Create a simple AI agent")

    manager.update_status(task_id=task1.id,status=TaskStatus.RUNNING)

    agent_state = AgentState(current_task=task1,task_count=len(manager.tasks),workspace=workspace)

    print("\nAgent State:")
    print(agent_state)

    print("\nAll Tasks:")

    for tasks in manager.list_tasks():
        print (tasks)
    
    manager.save_tasks(tasks_dir/"tasks.json")

    print("Tasks saved successfully!")

