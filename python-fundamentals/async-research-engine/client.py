import httpx
import asyncio
from decorators import retry
from decorators import log_execution
from decorators import timer

@log_execution
@retry(max_tries=3)
async def fetch_data(url) :
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

        return data

@timer
async def fetch_all(urls):

    tasks = [fetch_data(url) for url in urls]

    results = await asyncio.gather(*tasks,return_exceptions=True)

    processed_results = []

    for url,result in zip(urls,results):

        if isinstance(result, Exception):
            processed_results.append(
                {
                    "url": url,
                    "status": "failed",
                    "error_type": type(result).__name__,
                    "error": str(result)
                }
            )

        else:
            processed_results.append(result)

    return processed_results
