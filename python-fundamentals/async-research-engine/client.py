import httpx
import asyncio
from decorators import retry

@retry(max_tries=3)
async def fetch_data(url) :
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

        return data

async def fetch_all(urls):

    tasks = [fetch_data(url) for url in urls]

    results = await asyncio.gather(*tasks,return_exceptions=True)

    processed_results = []

    for result in results:

        if isinstance(result, Exception):
            processed_results.append(
                {
                    "status": "failed",
                    "error": str(result)
                }
            )

        else:
            processed_results.append(result)

    return processed_results
