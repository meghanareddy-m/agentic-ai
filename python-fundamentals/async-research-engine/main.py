import asyncio
from client import fetch_all
from utils import save_results
from utils import stream_results

async def main():
    urls = [
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
    "https://bad-url-12345.com"
    ]
    
    results = await fetch_all(urls)
    save_results(results)
    for result in stream_results(results):
        print(result)

asyncio.run(main())