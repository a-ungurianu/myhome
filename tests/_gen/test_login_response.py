"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import myhome._gen
from myhome._gen.model.access_status import AccessStatus

globals()["AccessStatus"] = AccessStatus
from myhome._gen.model.login_response import LoginResponse


class TestLoginResponse(unittest.TestCase):
    """LoginResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLoginResponse(self):
        """Test LoginResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LoginResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()