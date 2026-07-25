# Agent Research Vault

## Overview

Agent Research Vault is an AI-inspired research memory system that collects information from real online sources, validates it using Pydantic, stores it persistently, and allows future retrieval.

This project was built as a capstone to demonstrate the practical application of Python fundamentals, asynchronous programming, API integration, Pydantic validation, exception handling, JSON-based persistence, and basic agent-oriented system design. The goal was to combine concepts learned across previous projects into a single end-to-end research workflow.

## Features

- Async research using asyncio
- HackerNews integration
- GitHub repository search
- Pydantic validation
- Persistent JSON storage
- Topic-based search
- Analytics dashboard

## Tech Stack

- Python
- Asyncio
- HTTPX
- Pydantic
- JSON Storage

## Project Architecture

User
↓
ResearchAgent
↓
ResearchClient
↓
External APIs
↓
ResearchSession
↓
ResearchStorage
↓
research_db.json

## Installation

pip install -r requirements.txt

## Run

python main.py