from client import ResearchClient
from models import ResearchSession

class ResearchAgent:
    def __init__(self):
        self.client =ResearchClient()

    async def research(self,topic:str)->ResearchSession:
        results = await self.client.search_all(topic)

        session = ResearchSession(topic=topic,results=results)

        return session
    