from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    contents: str
    is_done: bool


class SignUpRequest(BaseModel):
    username: str
    password: str
