import os
import json

import requests
from unittest import TestCase

TESTS_BASE_PATH = os.path.abspath(os.path.dirname(__file__))


class BaseTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _build_mocked_response(self, status_code=200, content=None):
        """ Returns a Response objects, opcionally with custom
            content and status_code
        """
        response = requests.Response()
        response.status_code = status_code
        if content is not None:
            response._content = json.dumps(content)
        return response
