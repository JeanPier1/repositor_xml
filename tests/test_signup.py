import unittest
import json

from app import app
from tests.BaseCase import BaseCase


class SignupTest(BaseCase):

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email": "paolo@gmail.com",
            "password": "12345678"
        })

        # When
        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
