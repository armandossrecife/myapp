from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
  id: int
  username: str
  email: str
  password: str

class UserLogin(BaseModel):
  username: str
  password: str

class UserPassword(BaseModel):
  username: str
  password: str
  confirm_password: str

class Note(BaseModel):
  id: int
  description: str
  created_at: datetime
  user_id: int

class NewNote(BaseModel):
  description: str
  username: str