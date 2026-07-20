from models.agent import Agent, AgentRole
from models.task import Task
from orchestrator.manager import Manager
from storage.json_store import JsonStore
from tools.search_tool import SearchTool


def main():

    manager = Manager()

    agent = Agent(name="Research Agent",role=AgentRole.RESEARCH,skills=["Python", "Research"],max_tasks=3)

    manager.create_agent(agent)

    task = Task(title="Research LangGraph",description="Learn LangGraph basics")

    manager.create_task(task)

    manager.assign_task(task, agent)

    result = manager.complete_task(task=task,agent=agent,output="LangGraph research completed successfully",execution_time=2.5)

    print("Result Created:")
    print(result)

    task_dict = task.model_dump()

    print("\nTask as Dictionary:")
    print(task_dict)

    recreated_task = Task.model_validate(task_dict)

    print("\nRecreated Task:")
    print(recreated_task)

    store = JsonStore()

    store.save(
        "tasks.json",
        {
            str(task.task_id): task.model_dump(mode="json")
        }
    )

    print("\nTask saved to tasks.json")

    tool = SearchTool()
    search_result = tool.search("LangGraph")

    print("\nSearch Tool:")
    print(search_result)


if __name__ == "__main__":
    main()