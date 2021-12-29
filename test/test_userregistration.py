import unittest
from user_registration import UserRegistration
from UserRegistrationException import UserRegistrationException

class TestUserRegistration(unittest.TestCase):
    def test_first_name_valid(self):
        expected = "Geeta"
        object_user = UserRegistration()
        object_user.first_name_set(expected)
        self.assertEqual(expected, object_user.first_name_get())

    def test_first_name_invalid(self):
        expected = "geeta"
        object_user = UserRegistration()
        try:
            object_user.first_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("first name invalid", exception.__str__())

    def test_first_name_empty(self):
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.first_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid first name, it should not be empty", exception.__str__())

    def test_last_name_valid(self):
        expected = "Madabalmath"
        object_user = UserRegistration()
        object_user.last_name_set(expected)
        self.assertEqual(expected, object_user.last_name_get())

    def test_last_name_invalid(self):
        expected = "madabalmath"
        object_user = UserRegistration()
        try:
            object_user.last_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("last name invalid", exception.__str__())

    def test_last_name_empty(self):
        expected = ""
        object_user = UserRegistration()
        try:
            object_user.last_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid Last name, it should not be empty", exception.__str__())

    def test_mobile_number_valid(self):
        expected = "9972630725"
        object_user = UserRegistration()
        object_user.mobile_number_set(expected)
        self.assertEqual(expected, object_user.mobile_number_get())

    def test_mobile_number_invalid(self):
        expected = "997263072"
        object_user = UserRegistration()
        try:
            object_user.mobile_number_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Mobile number is invalid", exception.__str__())

    def test_mobile_number_empty(self):
        expected = ""
        object_user = UserRegistration()
        try:
            object_user.mobile_number_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid mobile number ,it should not be empty", exception.__str__())

    def test_password_valid(self):
        expected = "1234567891"
        object_user = UserRegistration()
        object_user.password_set(expected)
        self.assertEqual(expected, object_user.password_get())

    def test_first_n_invalid(self):
        expected = "123456789"
        object_user = UserRegistration()
        try:
            object_user.password_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("password is invalid", exception.__str__())

    def test_password_empty(self):
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.password_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid password, it should not be empty", exception.__str__())
