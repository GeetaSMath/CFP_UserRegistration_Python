import unittest

from parameterized import parameterized
from user_registration import UserRegistration
from UserRegistrationException import UserRegistrationException

class TestUserRegistration(unittest.TestCase):
    """
    class: created Test case TestUserRegistration
    """

    def setUp(self):
        self.object_user = UserRegistration()

    def test_first_name_valid(self):
        """
         test_first_name: validating firstname :Geeta
        :return: Geeta pass the test case
        """
        expected = "Geeta"
        self.object_user.first_name_set(expected)
        self.assertEqual(expected, self.object_user.first_name_get())

    def test_first_name_invalid(self):
        """
         created function to test_name for invalid
        :return: "geeta" case should be fail
        """
        expected = "geeta"

        try:
            self.object_user.first_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("first name invalid", exception.__str__())

    def test_first_name_empty(self):
        """
          test_first_name to check for empty test
          :return: empty test and test will pass
          """

        expected = ''
        try:
            self.object_user.first_name_set(expected)
        except UserRegistrationException as exception:
         self.assertEqual("Enter valid first name, it should not be empty", exception.__str__())


    def test_last_name_valid(self):
            """
                test_last_name to valid
                :return: pass testcase for valid expected
              """
            expected = "Madabalmath"
            try:
                self.object_user.first_name_set(expected)
            except UserRegistrationException as exception:
                self.assertEqual("Enter valid last name", exception.__str__())


    def test_last_name_invalid(self):
        """
        test_last_time to test for invalid
        :return: pass testcase for invalid
        """
        expected = "madabalmath"
        try:
            self.object_user.last_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("last name invalid", exception.__str__())


    def test_last_name_empty(self):
        """
         test_last_name to pass test case for empty
        :return: pass test case for none
        """
        expected = ""
        try:
            self.object_user.last_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid Last name, it should not be empty", exception.__str__())


    def test_mobile_number_valid(self):
        """
         test_mobile_number to validating expected
          :return: valid mobile number pass test case
          """
        expected = "9972630725"
        try:
            self.object_user.mobile_number_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid number", exception.__str__())


    def test_mobile_number_invalid(self):
        """
        test_mobile_number_invalid
        :return: invalid
        """
        expected = "997263072"

        try:
            self.object_user.mobile_number_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Mobile number is invalid", exception.__str__())

    def test_mobile_number_empty(self):
        """
         test_last_name to pass test case for empty
        :return: pass test case for none
        """
        expected = ""

        try:
            self.object_user.mobile_number_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid mobile number ,it should not be empty", exception.__str__())

    def test_password_valid(self):
        """
         test_password_valid : test case will pass
        :return: valid
        """
        expected = "1234567891"
        try:
            self.object_user.password_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("password must be valid one", exception.__str__())


    def test_password_invalid(self):
        """
          test_password_invalid: pass test case
            :return: invalid
            """
        expected = "123456789"

        try:
            self.object_user.password_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("password is invalid", exception.__str__())

    def test_password_empty(self):
        """
       test_password_empty: to pass test case for none
       :return: pass test case for none
       """

        expected = ''
        try:
            self.object_user.password_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid password, it should not be empty", exception.__str__())

class test_UserRegistration(unittest.TestCase):
    @parameterized.expand([
        ("Geetasmath123@gmail.com", "Geetasmath123@gmail.com"),
        ("g", "email_id is invalid"),
        ("", "Enter valid email_id, it should not be empty"),
    ])

    def test_email_id(self, input, expected):
        """

        :param input:input passing email_id
        :param expected: to make it valid expected
        :return:retrun valid email-id
        """
        object = UserRegistration()
        try:
            object.email_id_set(input)
            self.assertEqual(object.email_id_get(), expected)
        except UserRegistrationException as exception:
            self.assertEqual(expected, exception.__str__())

    @parameterized.expand([
        ("Geeta1@math", "Geeta1@math"),
        ("123", "password is invalid"),
        ("", "Enter valid password, it should not be empty"),
    ])
    def test_password(self, input, expected):
        """

        :param input: password as input as Geeta1@math expected same because to make it valid
        :param expected: Geeta1@math,inavlid,empty
        :return: first will return valid second for inavlid and password for empty
        """

        try:
            self.object.password_set(input)
            self.assertEqual(object.password_get(), expected)
        except UserRegistrationException as exception:
            self.assertEqual(expected, exception.__str__())

