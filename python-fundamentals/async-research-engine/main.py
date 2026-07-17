import asyncio
from client import fetch_all

async def main():
    urls = [
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
    "https://bad-url-12345.com"
    ]
    
    results = await fetch_all(urls)
    for result in results:
        print(result)

asyncio.run(main())