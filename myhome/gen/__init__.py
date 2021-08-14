# flake8: noqa

"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""



__version__ = "1.0.0"

# import apis into sdk package
from myhome.gen.api.default_api import DefaultApi

# import ApiClient
from myhome.gen.api_client import ApiClient
from myhome.gen.configuration import Configuration
from myhome.gen.exceptions import (
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from myhome.gen.models.action import Action
from myhome.gen.models.event import Event
from myhome.gen.models.get_actual_user_response import GetActualUserResponse
from myhome.gen.models.get_role_user_response import GetRoleUserResponse
from myhome.gen.models.init_check_response import InitCheckResponse
from myhome.gen.models.login_request import LoginRequest
from myhome.gen.models.login_response import LoginResponse
from myhome.gen.models.object_info import ObjectInfo
from myhome.gen.models.object_value import ObjectValue
from myhome.gen.models.object_value_dimmer import ObjectValueDimmer
from myhome.gen.models.object_value_light import ObjectValueLight
from myhome.gen.models.object_value_shutter import ObjectValueShutter
from myhome.gen.models.object_value_thermostat import ObjectValueThermostat
from myhome.gen.models.room import Room
from myhome.gen.models.serial_server import SerialServer
from myhome.gen.models.set_object_value_request import SetObjectValueRequest
from myhome.gen.models.set_object_value_response import SetObjectValueResponse
from myhome.gen.models.specific_object_request import SpecificObjectRequest
from myhome.gen.models.system_info import SystemInfo
from myhome.gen.models.zone import Zone
