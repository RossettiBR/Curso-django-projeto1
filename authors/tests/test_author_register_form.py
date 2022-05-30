from authors.forms import RegisterForm
from django.test import TestCase


class AuthorReisterFormUnitTest(TestCase):
    def test_first_name_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['first_name'].field.widget.attrs['placeholder']

        self.assertEqual('Ex.:John', placeholder)
