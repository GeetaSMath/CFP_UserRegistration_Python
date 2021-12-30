import math
import unittest

import parameterized

from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class
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
        object_user = UserRegistration()
        try:
            object_user.first_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("first name invalid", exception.__str__())

    def test_first_name_empty(self):
        """
          test_first_name to check for empty test
          :return: empty test and test will pass
          """

        expected = ''
        object_user = UserRegistration()
        try:
            object_user.first_name_set(expected)
        except UserRegistrationException as exception:
         self.assertEqual("Enter valid first name, it should not be empty", exception.__str__())


    def test_last_name_valid(self):
            """
                test_last_name to valid
                :return: pass testcase for valid expected
              """
            expected = "Madabalmath"
            self.object_user.first_name_set(expected)
            self.assertEqual(expected, self.object_user.first_name_get())


    def test_last_name_invalid(self):
        """
        test_last_time to test for invalid
        :return: pass testcase for invalid
        """
        expected = "madabalmath"
        object_user = UserRegistration()
        try:
            object_user.last_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("last name invalid", exception.__str__())


    def test_last_name_empty(self):
        """
         test_last_name to pass test case for empty
        :return: pass test case for none
        """
        expected = ""
        object_user = UserRegistration()
        try:
            object_user.last_name_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid Last name, it should not be empty", exception.__str__())


    def test_mobile_number_valid(self):
        """
         test_mobile_number to validating expected
          :return: valid mobile number pass test case
          """
        expected = "9972630725"
        self.object_user.mobile_number_set(expected)
        self.assertEqual(expected, self.object_user.mobile_number_get())


    def test_mobile_number_invalid(self):
        """
        test_mobile_number_invalid
        :return: invalid
        """
        expected = "997263072"
        object_user = UserRegistration()
        try:
            object_user.mobile_number_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Mobile number is invalid", exception.__str__())

    def test_mobile_number_empty(self):
        """
         test_last_name to pass test case for empty
        :return: pass test case for none
        """
        expected = ""
        object_user = UserRegistration()
        try:
            object_user.mobile_number_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid mobile number ,it should not be empty", exception.__str__())

    def test_password_valid(self):
        """
         test_password_valid : test case will pass
        :return: valid
        """
        expected = "1234567891"
        self.object_user.password_set(expected)
        self.assertEqual(expected, self.object_user.password_get())


    def test_password_invalid(self):
        """
          test_password_invalid: pass test case
            :return: invalid
            """
        expected = "123456789"
        object_user = UserRegistration()
        try:
            object_user.password_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("password is invalid", exception.__str__())

    def test_password_empty(self):
        """
       test_password_empty: to pass test case for none
       :return: pass test case for none
       """

        expected = ''
        object_user = UserRegistration()
        try:
            object_user.password_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual("Enter valid password, it should not be empty", exception.__str__())

class Test_UserRegistration(unittest.TestCase):
    @parameterized.expand([
        ("valid", "Geetasmath123@gmail.com", "Geetasmath123@gmail.com"),
        ("invalid", "geetasmath@gmail.com", "geetasmath123@gmail.com"),
        ("empty", "", ""),
    ])
    def test_email_id(self,email_id, input, expected):
        input = UserRegistration()
        try:
            input.email_id_set(expected)
        except UserRegistrationException as exception:
            self.assertEqual(UserRegistration.email_id_get(input), exception.__str__())
