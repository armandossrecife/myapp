import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()

class UserDB(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)
  password_hash = Column(String)
  # Cria um relacionamento com a classe Note
  notes = relationship("Note")

class ImageProfile(Base):
    __tablename__ = "image_profile"
    # Define a chave estrangeira (FK) para a tabela users
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    name = Column(String(250), nullable=False)
    # Optional: Add a field to store the image file path
    file_path = Column(String(250))

# Note model
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True) 
    description = Column(String(1000))
    created_at = Column(DateTime, default=datetime.now())
    # Define a chave estrangeira (FK) para a tabela users
    user_id = Column(Integer, ForeignKey("users.id"))