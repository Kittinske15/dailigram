from django.test import TestCase
from django import forms
from diary.forms import UserForm

class TestingForms(TestCase):

    def test_valid_user_forms(self):
        """
        Test the valid user form data.
        """

        form = UserForm(
            data={'username': "user", 'password': "user", 'email': "user@gmail.com"})
        self.assertTrue(form.is_valid())

    def test_invalid_user_forms(self):
        """
        Test the invalid user form data. 
        """

        form = UserForm(
            data={'username': "", 'password': "", 'email': "", 'first_name': ""})
        self.assertFalse(form.is_valid())

    def test_valid_page_forms(self):

    


    
