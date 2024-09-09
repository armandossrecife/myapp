import unittest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app import banco
from app import modelos
from app import entidades

import HtmlTestRunner

# Create a clean database
engine = create_engine(banco.DATABASE_URL)
Session = sessionmaker(autocommit=False, bind=engine)
modelos.Base.metadata.drop_all(engine)
modelos.Base.metadata.create_all(bind=engine)

class NoteDAOTest(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        self.note_dao = banco.NoteDAO(self.session)
        self.user_dao = banco.UserDAO(self.session)

    def tearDown(self):
        self.session.close()

    def test_create_note(self):
        # Create a user first
        db_user = entidades.User(id=1, username="notauser1", email="notauser1@g.com", password="123456")
        user = self.user_dao.create_user(db_user)

        # Create a note
        note = self.note_dao.create_note(user.id, 'This is a test note1')

        self.assertIsNotNone(note)
        self.assertEqual(note.description, 'This is a test note1')
        self.assertEqual(note.user_id, user.id)

    def test_get_all_notes(self):
        # Create a user and 2 notes
        db_user2 = entidades.User(id=2, username="notauser2", email="notauser2@g.com", password="123456")
        user = self.user_dao.create_user(db_user2)
        self.note_dao.create_note(user.id, 'Note 2')
        self.note_dao.create_note(user.id, 'Note 3')

        notes = self.note_dao.get_all_notes()
        
        # two notes plus one note created aforementioned
        self.assertEqual(len(notes), 3)

    def test_get_note_by_id(self):
        # Create a note
        db_user3 = entidades.User(id=3, username="notauser3", email="notauser3@g.com", password="123456")
        user = self.user_dao.create_user(db_user3)
        note = self.note_dao.create_note(user.id, 'Test Note')

        found_note = self.note_dao.get_note_by_id(note.id)

        self.assertEqual(found_note.id, note.id)

    def test_get_notes_by_user_id(self):
        # Create a user and multiple notes
        db_user4 = entidades.User(id=4, username="notauser4", email="notauser4@g.com", password="123456")
        user = self.user_dao.create_user(db_user4)
        self.note_dao.create_note(user.id, 'Note A')
        self.note_dao.create_note(user.id, 'Note B')

        notes = self.note_dao.get_notes_by_user_id(user.id)

        self.assertEqual(len(notes), 2)

    def test_update_note(self):
        # Create a note
        db_user5 = entidades.User(id=5, username="notauser5", email="notauser5@g.com", password="123456")
        user = self.user_dao.create_user(db_user5)
        note = self.note_dao.create_note(user.id, 'Original Note')

        updated_note = self.note_dao.update_note(note.id, 'Updated Note')

        self.assertEqual(updated_note.description, 'Updated Note')

    def test_delete_note(self):
        # Create a note
        db_user6 = entidades.User(id=6, username="notauser6", email="notauser6@g.com", password="123456")
        user = self.user_dao.create_user(db_user6)
        note = self.note_dao.create_note(user.id, 'Note to Delete')

        deleted = self.note_dao.delete_note(note.id)

        self.assertTrue(deleted)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
