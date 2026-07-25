import asyncio
import httpx
from models import ResearchResult

class APIServiceUnavailableError(Exception):
        pass

class ResearchClient:

    async def search_hackernews(self, topic: str) ->list[ResearchResult]:
        url = f"https://hn.algolia.com/api/v1/search?query={topic}"
        valid_responses=[]

        async with httpx.AsyncClient() as client:
            try:    
                response= await client.get(url)
            except httpx.HTTPError as e:
                raise APIServiceUnavailableError(f"HackerNews unavailable: {e}" )
            

            if response.status_code == 200:
                data=response.json()
                for item in data.get("hits",[])[:5]:
                    title=item.get("title")
                    link=item.get("url")

                    if title and link:
                        valid_responses.append(ResearchResult(title=title,url=link,source="HackerNews"))

            return valid_responses

    async def search_github(self,topic:str)->list[ResearchResult]:
        url = f"https://api.github.com/search/repositories?q={topic}"
        valid_responses=[]

        async with httpx.AsyncClient() as client:
            try:    
                response= await client.get(url)
            except httpx.HTTPError as e:
                raise APIServiceUnavailableError(f"GitHub unavailable: {e}" )

            if response.status_code==200:
                data=response.json()
                for repo in data.get("items",[])[:5]:
                    title=repo.get("name")
                    link=repo.get("html_url")

                    if title and link:
                        valid_responses.append(ResearchResult(title=title,url=link,source="GitHub"))

            return valid_responses

    async def search_all(self,topic:str)->list[ResearchResult]:
        gather_results=await asyncio.gather(self.search_github(topic),self.search_hackernews(topic),return_exceptions=True)

        combined_results=[]

        for result in gather_results:
            if isinstance(result,Exception):
                continue

            combined_results.extend(result)

        if not combined_results:
            raise APIServiceUnavailableError("All research sources are unavailable")
        return combined_results
