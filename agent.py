from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from tools import error, complate
from Agent_prompt import before_chat_prompt
from llama_index.core import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chatbot(question: str = Form(...)):
    try:
        react_system_prompt = PromptTemplate(before_chat_prompt)
        agent = ReActAgent.from_tools([error, complate], llm=OpenAI(model="gpt-4o"), verbose=True)
        agent.update_prompts({"agent_worker:system_prompt": react_system_prompt})
        response = agent.chat(question)
        return JSONResponse(content={"response": response.response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
