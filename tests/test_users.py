import os
import json
import requests
from unittest import TestCase
from mock import patch

from mercadolibre import api
from mercadolibre import http
from tests import TESTS_BASE_PATH


APP_ID = 'SOME_APP_ID'
APP_SECRET = 'SOME_APP_SECRET'
ACCESS_TOKEN = "SOME_VALID_ACCESS_TOKEN"


class UserResourceTestCase(TestCase):
    def setUp(self):
        self.session = http.get_session()

    def _build_mocked_response(self, status_code=200, content=None):
        """ Returns a Response objects, opcionally with custom
            content and status_code
        """
        response = requests.Response()
        response.status_code = status_code
        if content is not None:
            response._content = json.dumps(content)
        return response

    def test_me(self):
        """Should return UserResource with current user data when me() method is called"""
        ml = api.login(APP_ID, APP_SECRET, ACCESS_TOKEN)
        with open(os.path.join(TESTS_BASE_PATH, 'fixtures/users_me.json')) as f:
            fixture = json.loads(f.read())
        with patch.object(requests.Session, 'get') as mocked:
            mocked.return_value = self._build_mocked_response(content=fixture)
            me = ml.me()
        self.assertEqual(str(me.id), '107531232')
        self.assertEqual(me.email, 'test.user@test.com')
        self.assertEqual(me.nickname, 'TEST USER')
        self.assertEqual(me.first_name, 'Test')
        self.assertEqual(me.last_name, 'User')
        self.assertEqual(me.site_id, 'MLA')
