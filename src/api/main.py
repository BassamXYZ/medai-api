from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from hack4syria_medai.crew import Hack4SyriaMedai


load_dotenv(override=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    user_question: str


class TaskOutput(BaseModel):
    task_name: str
    task_description: str
    task_output: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/chat")
def chat(question: Question) -> list[TaskOutput]:
    input = {"topic": question.user_question}
    result = Hack4SyriaMedai().crew().kickoff(inputs=input)
    tasks_output = []
    for task_output in result.tasks_output:
        tasks_output.append(TaskOutput(
            task_name=task_output.name, task_description=task_output.description, task_output=task_output.raw))

    return tasks_output
