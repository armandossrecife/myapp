from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import utilidades
from app import entidades
from app import modelos
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "sqlite:///users.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    print("Recriando as tabelas...")
    modelos.Base.metadata.drop_all(engine)
    modelos.Base.metadata.create_all(bind=engine)
    print("Tables criadas")

def get_db():
  db = SessionLocal()
  try:
    yield db # TODO: revisar o fechamento das sessoes de banco abertas na instancia da aplicacao
  finally:
    db.close()

### Users operations ###
class UserDAO:
  def __init__(self, db):
    self.db = db
  
  def get_user(self,username):
    try: 
      user = self.db.query(modelos.UserDB).filter(modelos.UserDB.username == username).first()
      return user
    except SQLAlchemyError as sqlerror:
      raise ValueError(f'Erro ao consultar usuario {username}: {str(sqlerror)}')
     
  def get_user_by_id(self, user_id: int):
    try:
      user = self.db.query(modelos.UserDB).filter(modelos.UserDB.id == user_id).first()
      return user
    except SQLAlchemyError as sqlerror:
      print(type(sqlerror))
      raise ValueError(f"Erro ao consultar usuario: {str(sqlerror)}")

  def create_user(self, user: entidades.User):
    try:
      db = SessionLocal()
      hashed_password = utilidades.hash_password(user.password)
      db_user = modelos.UserDB(username=user.username, email=user.email, password_hash=hashed_password)
      db.add(db_user)
      db.commit()
      db.refresh(db_user)
      return entidades.User(id=db_user.id, username=db_user.username, email=db_user.email, password=user.password)
    except SQLAlchemyError as sqlerror:
      print(type(sqlerror))
      raise ValueError(f"Erro ao criar usuário: {str(sqlerror)}")
    except Exception as ex:
      raise ValueError(f"Erro ao criar usuário: {str(ex)}")

  def authenticate_user(self, username: str, password: str):
    try:
      user = self.get_user(username)
      if not user:
        return False
      if not utilidades.verify_password(password, user.password_hash):
        return False
      return user
    except SQLAlchemyError as sqlerror:
      print(type(sqlerror))
      raise ValueError(f"Erro ao autenticar usuário: {str(sqlerror)}")
    except Exception as ex:
      raise ValueError(f"Erro ao autenticar usuário: {str(ex)}")

  def get_all_users(self):
    """Retrieves all users from the database.
    Args:
        db: A database session object.
    Returns:
        A list of User objects representing all users in the database.
    """
    try:
      users = self.db.query(modelos.UserDB).all()
      return [entidades.User(id=user.id, username=user.username, email=user.email, password="?") for user in users]
    except SQLAlchemyError as sqlerror:
      print(type(sqlerror))
      raise ValueError(f"Erro ao recuperar usuários: {str(sqlerror)}")
    except Exception as ex:
      raise ValueError(f"Erro ao recuperar usuários: {str(ex)}")

  def get_image_profile_for_user(self, user_id: int):
    try: 
      image_profile = self.db.query(modelos.ImageProfile).get(user_id)
      if image_profile:
        image_name = image_profile.name
        return image_name
      else:
        return "default.png"
    except SQLAlchemyError as sqlerror:
      print(type(sqlerror))
      raise ValueError(f'Erro ao fazer a busca da imagem {str(sqlerror)}')

  def add_profile_image_to_user(self, user_id: int, filename: str):
    try:
      existing_image = self.get_image_profile_for_user(user_id)
      if existing_image:
          # Update existing image record
          update_image = modelos.ImageProfile(user_id=user_id, name=filename)
          self.db.merge(update_image)
      else:
          # Create a new image record
          new_image = modelos.ImageProfile(user_id=user_id, name=filename)
          self.db.add(new_image)
      self.db.commit()
    except SQLAlchemyError as sqlerror:
      print(type(sqlerror))
      self.db.rollback()
      raise ValueError(f"Error adding profile image: {str(sqlerror)}")

  def update_password_user(self, user_id: int, new_password: str):
    """
    Updates the password for a user identified by user_id.

    Args:
        user_id: The ID of the user to update.
        new_password: The new password for the user.
    """
    try:
      user = self.get_user_by_id(user_id)
      if not user:
        raise ValueError(f"Usuário {user_id} inválido")
      hashed_password = utilidades.hash_password(new_password)
      user.password_hash = hashed_password
      self.db.merge(user)
      self.db.commit()
      self.db.refresh(user)
    except SQLAlchemyError as sqlerror:
      print(type(sqlerror))
      self.db.rollback()
      raise ValueError(f"Error updating user: {str(sqlerror)}")

# DAO (Data Access Object) for Note model
class NoteDAO:
    def __init__(self, db):
        self.db = db

    def create_note(self, user_id, description):
        db = SessionLocal()
        new_note = None
        try:
            new_note = modelos.Note(description=description, user_id=user_id)
            db.add(new_note)
            db.commit()
            db.refresh(new_note)
        except SQLAlchemyError as sqlerror:
            print(type(sqlerror))
            self.db.rollback()
            raise Exception(f'Erro ao criar nota: {str(sqlerror)}')
        return new_note

    def get_all_notes(self):
        try:
          notas = self.db.query(modelos.Note).all()
          return [entidades.Note(id=nota.id, description=nota.description, created_at=nota.created_at, user_id=nota.user_id) for nota in notas]
        except SQLAlchemyError as sqlerror:
          print(type(sqlerror))
          raise ValueError(f"Erro ao listar notas do usuário: {str(sqlerror)}")

    def get_note_by_id(self, note_id):
      try: 
        nota = self.db.query(modelos.Note).filter_by(id=note_id).first()
        return entidades.Note(id=nota.id, description=nota.description, created_at=nota.created_at, user_id=nota.user_id)
      except SQLAlchemyError as sqlerror:
        print(type(sqlerror))
        raise ValueError(f"Erro ao recuperar nota por id: {str(sqlerror)}")
      
    def get_notes_by_user_id(self, user_id):
      try:
        notas = self.db.query(modelos.Note).filter_by(user_id=user_id).all() 
        return [entidades.Note(id=nota.id, description=nota.description, created_at=nota.created_at, user_id=nota.user_id) for nota in notas]
      except SQLAlchemyError as sqlerror:
        print(type(sqlerror))
        raise ValueError(f"Erro ao recuperar notas do usuario: {str(sqlerror)}")
      
    def update_note(self, note_id, description):
      try:
        note = self.db.get(modelos.Note, note_id)
        if note:
            note.description = description
            self.db.commit()
            return entidades.Note(id=note.id, description=note.description, created_at=note.created_at, user_id=note.user_id)
        else:
            return None
      except SQLAlchemyError as sqlerror:
        print(type(sqlerror))
        self.db.rollback()
        raise ValueError(f"Erro ao atualizar nota: {str(sqlerror)}")

    def delete_note(self, note_id):
      try: 
        note = self.db.get(modelos.Note, note_id)
        if note:
            self.db.delete(note)
            self.db.commit()
            return True
        else:
            return False
      except SQLAlchemyError as sqlerror:
        print(type(sqlerror))
        self.db.rollback()
        raise ValueError(f"Erro ao deletar nota: {str(sqlerror)}")