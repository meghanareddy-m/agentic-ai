# AI Agent Task Orchestrator

A beginner-friendly multi-agent orchestration system built using Pydantic.

## Project Overview

This project shows how an AI orchestrator manages agents, tasks, execution results, and agent states.

The system allows:

- Creating Agents
- Creating Tasks
- Assigning Tasks to Agents
- Completing Tasks
- Tracking Results
- Managing Agent State
- Saving Data to JSON

---

## Project Structure

```text
ai-agent-task-orchestrator/
│
├── models/
│   ├── task.py
│   ├── agent.py
│   ├── result.py
│   └── agent_state.py
│
├── orchestrator/
│   └── manager.py
│
├── storage/
│   └── json_store.py
│
├── tools/
│   └── search_tool.py
│
├── tasks.json
│
└── main.py
```

---

## Models

### Task

Represents work that needs to be completed.

**Fields**

- task_id
- title
- description
- priority
- status
- created_at

### Agent

Represents an AI agent.

**Fields**

- agent_id
- name
- role
- skills
- max_tasks

### Result

Represents the output generated after task completion.

**Fields**

- result_id
- task
- agent
- output
- success
- execution_time
- completed_at

### AgentState

Tracks the current state of an agent.

**Fields**

- current_tasks
- completed_tasks
- active
- last_active
- total_completed_tasks

---

## Features

### Task Management

- Create Tasks
- Retrieve Tasks
- Assign Tasks
- Complete Tasks

### Agent Management

- Create Agents
- Retrieve Agents
- Track Agent State

### Result Tracking

- Store Execution Results
- Track Success Status
- Record Execution Time

### Storage

- Save Data to JSON
- Load Data from JSON

---

## Pydantic Concepts Used

- BaseModel
- Field
- Enums
- Nested Models
- List[NestedModel]
- Field Validators
- Computed Fields
- model_dump()
- model_validate()

---

## Example Workflow

```text
Create Agent
      ↓
Create Task
      ↓
Assign Task
      ↓
Execute Task
      ↓
Complete Task
      ↓
Generate Result
      ↓
Save Data
```

---

## Future Improvements

- Agent Selection Logic
- Automatic Task Routing
- Multi-Agent Collaboration
- Tool Registry
- Async Execution
- Database Storage

---

## Learning Objective

The primary purpose of this project is to learn how Pydantic is used to model and validate structured data in Agentic AI systems.