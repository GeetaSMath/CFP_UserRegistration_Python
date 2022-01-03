from nose_parameterized import parameterized
from UserRegistrationException import UserRegistrationException
import re

class UserRegistration:

    def setUp(self):
        self.object.user=UserRegistration()

    """
        class: created UserRegistration class
        implemented user infromation,by validation part include regex
        and exception to raise exception.
    """

    def first_name_get(self):
        return self.first_name

    def first_name_set(self, first_name):
        """
        :param first_name: using def function created first name
        :return:
        """
        if first_name == "":
            raise UserRegistrationException("Enter valid first name, it should not be empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", first_name):
            self.first_name = first_name
        else:
            raise UserRegistrationException('first name invalid')

    def last_name_get(self):
        return self.last_name

    def last_name_set(self, last_name):
        """

        :param last_name: using last_name set used def function
        :return:
        """
        if last_name == "":
            raise UserRegistrationException("Enter valid Last name, it should not be empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", last_name):
            self.last_name = last_name
        else:
            raise UserRegistrationException('last name invalid')

    def mobile_number_get(self):
        return self.mobile_number

    def mobile_number_set(self, mobile_number):
        """
        :param mobile_number: mobile number
        :return:mobile number
        """
        if mobile_number == "":
            raise UserRegistrationException("Enter valid mobile number ,it should not be empty")
        if re.fullmatch("^([91]{2}[ ])?[0-9]{10}$", mobile_number):
            self.mobile_number= mobile_number
        else:
            raise UserRegistrationException('Mobile number is invalid')

    def password_get(self):
        return self.password

    def password_set(self, password):
        """
        :param password: param as password
        :return:password by following validation
        """
        if password == "":
            raise UserRegistrationException("Enter valid password, it should not be empty")
        if re.fullmatch("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", password):
            self.password = password
        else:
            raise UserRegistrationException('password is invalid')

    def email_id_get(self):
        return self.email_id

    def email_id_set(self, email_id):
        """
         :param email_id:
        :return:email_id by follwoing validation
        """
        if email_id == "":
            raise UserRegistrationException("Enter valid email_id, it should not be empty")
        if re.fullmatch("^[a-zA-z0-9]+([.][0-9a-zA-z]+)*@[a-zA-z]+.[a-z]{2,3}([.][a-z]{2,3})*$", email_id):
            self.email_id = email_id
        else:
            raise UserRegistrationException("email_id is invalid")



