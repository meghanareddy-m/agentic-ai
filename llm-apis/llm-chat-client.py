import httpx
import asyncio
from pydantic import BaseModel

url="http://localhost:11434/api/chat"

class Message(BaseModel):
    role:str
    content:str

class Options(BaseModel):
    temperature: float
    num_predict: int
    stop: list[str]

class ChatRequest(BaseModel):
    model:str
    stream : bool = False
    messages: list[Message]
    options: Options

class ChatResponse(BaseModel):
    model:str
    created_at:str
    message:Message
    done:bool

memory : list[Message] =[]

def weather(city):
    pass

def add_system():
    memory.append( Message(role="system",content="You are a helpful AI Assistant") )

def add_user(query):
    memory.append(Message(role="user",content=query))

def add_assistant(response):
    memory.append(Message(role="assistant",content=response))

def get_messages()->list[Message]:
    return memory


async def main():
    async with httpx.AsyncClient(timeout=None) as client:
        add_system()
        while True:
            q = input("you: ")
            if(q.lower().strip()=="bye"):
                break

            add_user(q)

            request=ChatRequest(
                model="qwen3.5:9b",
                stream=False,
                messages=get_messages(),
                options=Options(temperature=0.3,num_predict=1000,stop=["you: "])
            )

            
            response=await client.post(url,json=request.model_dump())

            data=response.json()
            valid_response=ChatResponse.model_validate(data)
            assis_data=valid_response.message.content
            add_assistant(assis_data)
            print(f"AI : {assis_data}")



asyncio.run(main())