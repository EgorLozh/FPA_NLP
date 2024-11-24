from pydantic import BaseModel


class VideoSchema(BaseModel):
    url: str


class ScriptActionSchema(BaseModel):
    text: str
    weight: int


class CheckedScriptActionSchema(BaseModel):
    text: str
    weight: int
    check: bool


class RequestSchema(BaseModel):
    id: str
    video: VideoSchema
    actions: list[ScriptActionSchema]


class ReportSchema(BaseModel):
    request_id: str
    total_score: int
    actions: list[CheckedScriptActionSchema]

class MessageSchema(BaseModel):
    type: str


class RequestMessageSchema(MessageSchema):
    data: RequestSchema


class ReportMessageSchema(MessageSchema):
    data: ReportSchema
