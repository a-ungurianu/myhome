# -*- coding: utf-8 -*-

"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from myhome.gen.configuration import Configuration


class SystemInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"pin_code": "str", "serial_server": "str", "version_server": "str"}

    attribute_map = {
        "pin_code": "pinCode",
        "serial_server": "serialServer",
        "version_server": "versionServer",
    }

    def __init__(
        self,
        pin_code=None,
        serial_server=None,
        version_server=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SystemInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pin_code = None
        self._serial_server = None
        self._version_server = None
        self.discriminator = None

        if pin_code is not None:
            self.pin_code = pin_code
        if serial_server is not None:
            self.serial_server = serial_server
        if version_server is not None:
            self.version_server = version_server

    @property
    def pin_code(self):
        """Gets the pin_code of this SystemInfo.  # noqa: E501

        OpenWebNet password  # noqa: E501

        :return: The pin_code of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._pin_code

    @pin_code.setter
    def pin_code(self, pin_code):
        """Sets the pin_code of this SystemInfo.

        OpenWebNet password  # noqa: E501

        :param pin_code: The pin_code of this SystemInfo.  # noqa: E501
        :type: str
        """

        self._pin_code = pin_code

    @property
    def serial_server(self):
        """Gets the serial_server of this SystemInfo.  # noqa: E501

        Serial number of server  # noqa: E501

        :return: The serial_server of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._serial_server

    @serial_server.setter
    def serial_server(self, serial_server):
        """Sets the serial_server of this SystemInfo.

        Serial number of server  # noqa: E501

        :param serial_server: The serial_server of this SystemInfo.  # noqa: E501
        :type: str
        """

        self._serial_server = serial_server

    @property
    def version_server(self):
        """Gets the version_server of this SystemInfo.  # noqa: E501

        Firmware version of server  # noqa: E501

        :return: The version_server of this SystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_server

    @version_server.setter
    def version_server(self, version_server):
        """Sets the version_server of this SystemInfo.

        Firmware version of server  # noqa: E501

        :param version_server: The version_server of this SystemInfo.  # noqa: E501
        :type: str
        """

        self._version_server = version_server

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SystemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemInfo):
            return True

        return self.to_dict() != other.to_dict()
