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

class UserDAOTest(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        self.user_dao = banco.UserDAO(self.session)

    def tearDown(self):
        self.session.close()

    def test_create_user(self):
        # Create a user
        user = entidades.User(id=1, username="test_user", email="test_user@example.com", password="password123")
        created_user = self.user_dao.create_user(user)
        user_with_password_hash = self.user_dao.get_user_by_id(created_user.id)

        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.username, user.username)
        self.assertEqual(created_user.email, user.email)
        # Ensure password is hashed
        self.assertNotEqual(user_with_password_hash.password_hash, user.password)

    def test_get_user(self):
        # Create a user
        user = entidades.User(id=2, username="test_user2", email="test_user2@example.com", password="password123")
        self.user_dao.create_user(user)

        found_user = self.user_dao.get_user(user.username)

        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.username, user.username)
        self.assertEqual(found_user.email, user.email)

    def test_get_user_by_id(self):
        # Create a user
        user = entidades.User(id=3, username="test_user3", email="test_user3@example.com", password="password123")
        created_user = self.user_dao.create_user(user)

        found_user = self.user_dao.get_user_by_id(created_user.id)

        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.id, created_user.id)
        self.assertEqual(found_user.username, user.username)

    def test_authenticate_user(self):
        # Create a user
        user = entidades.User(id=4, username="test_user4", email="test_user4@example.com", password="password123")
        self.user_dao.create_user(user)

        authenticated_user = self.user_dao.authenticate_user(user.username, user.password)

        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user.username, user.username)

        # Test incorrect password
        self.assertEqual(self.user_dao.authenticate_user(user.username, "wrong_password"), False)

    def test_get_image_profile_for_user(self):
        # Create a user and associate a profile image
        user = entidades.User(id=8, username="test_user5", email="test_user5@example.com", password="password123")
        created_user = self.user_dao.create_user(user)
        self.user_dao.add_profile_image_to_user(created_user.id, "profile_image.jpg")

        image_name = self.user_dao.get_image_profile_for_user(created_user.id)

        self.assertEqual(image_name, "profile_image.jpg")

    def test_add_profile_image_to_user(self):
        # Create a user and add a profile image
        user = entidades.User(id=9, username="test_user6", email="test_user6@example.com", password="password123")
        created_user = self.user_dao.create_user(user)
        self.user_dao.add_profile_image_to_user(created_user.id, "profile_image2.jpg")

        image_name = self.user_dao.get_image_profile_for_user(created_user.id)

        self.assertEqual(image_name, "profile_image2.jpg")

    def test_update_password_user(self):
        # Create a user and update their password
        user = entidades.User(id=10, username="test_user7", email="test_user7@example.com", password="password123")
        created_user = self.user_dao.create_user(user)
        self.user_dao.update_password_user(created_user.id, "new_password")

        authenticated_user = self.user_dao.authenticate_user(created_user.username, "new_password")

        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user.username, created_user.username)

    def test_update_password_user_invalid_id(self):
        # Attempt to update the password of a non-existent user
        with self.assertRaises(ValueError):
            self.user_dao.update_password_user(999999, "new_password")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())