# Async Research Engine

A Python project inspired by modern AI systems that demonstrates asynchronous programming, concurrent API requests, decorators, generators, error handling, and JSON persistence.

## Features

- Concurrent API requests using `asyncio.gather()`
- Asynchronous HTTP client with `httpx.AsyncClient`
- Retry mechanism using a custom `@retry` decorator
- Execution logging with `@log_execution`
- Performance tracking with `@timer`
- Advanced error handling and recovery
- Result streaming using generators (`yield`)
- Save results to `results.json`

## Tech Stack

- Python 3
- asyncio
- httpx
- JSON

## Project Structure

```text
async-research-engine/
│
├── main.py
├── client.py
├── decorators.py
├── utils.py
├── engine.py
├── requirements.txt
├── results.json
└── README.md
```

## How It Works

```text
URLs
 ↓
fetch_all()
 ↓
asyncio.gather()
 ↓
fetch_data()
 ↓
HTTP Requests
 ↓
Process Results
 ↓
Save Results
 ↓
Stream Results
 ↓
Console Output
```

## Concepts Practiced

- Asynchronous Programming
- Concurrent Execution
- API Communication
- Custom Decorators
- Advanced Exception Handling
- Generators and `yield`
- JSON File Operations
- Project Organization

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Sample Output

```text
Starting fetch_data
Starting fetch_data
Starting fetch_data
Failed fetch_data
Completed fetch_data
Completed fetch_data

fetch_all took 2.56 seconds

Yielding result...
{user data}

Yielding result...
{user data}

Yielding result...
{
    'url': 'https://bad-url-12345.com',
    'status': 'failed',
    'error_type': 'ConnectError',
    'error': '[Errno 11001] getaddrinfo failed'
}
```

## Future Improvements

- ResearchEngine orchestration layer
- Dynamic URL input
- Async result streaming
- Request timeouts
- Structured logging
- Pydantic validation models

## Learning Outcomes

This project was built to practice:

- `async` / `await`
- `asyncio.gather()`
- `httpx.AsyncClient`
- Decorators
- Error handling and retries
- Generators
- JSON persistence
- Modular project structure