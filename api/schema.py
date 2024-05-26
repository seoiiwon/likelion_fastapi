from pydantic import BaseModel, field_validator
import datetime

class Post(BaseModel):
    id : int
    subject : str
    content : str
    date : datetime.datetime

# ========== CREATE SCHEMA ===========
class CreatePostSchema(BaseModel):
    subject : str
    content : str

    @field_validator("subject", "content")
    def empty_validation(cls, valid):
        if not valid or not valid.strip():
            raise ValueError("유효하지 않습니다.")
        return valid

# ========== UPDATE SCHEMA ==========
class UpdatePostSchema(CreatePostSchema):
    post_id : int

# ========== DELETE SCHEMA ==========
class DeletePostSchema(BaseModel):
    post_id : int


# ========== CREATE COMMENTS ==========
class CreateCommentSchema(BaseModel):
    content : str

    @field_validator("content")
    def empty_validation(cls, valid):
        if not valid or not valid.strip():
            raise ValueError("유효하지 않습니다.")
        return valid