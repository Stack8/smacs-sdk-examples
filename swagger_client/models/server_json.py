# coding: utf-8

"""
    SMACS REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 7.2.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServerJson(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'host_address': 'str',
        'description': 'str',
        'port': 'int',
        'server_type': 'str',
        'username': 'str',
        'password': 'str',
        'disabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'host_address': 'hostAddress',
        'description': 'description',
        'port': 'port',
        'server_type': 'serverType',
        'username': 'username',
        'password': 'password',
        'disabled': 'disabled'
    }

    def __init__(self, id=None, host_address=None, description=None, port=None, server_type=None, username=None, password=None, disabled=None):  # noqa: E501
        """ServerJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._host_address = None
        self._description = None
        self._port = None
        self._server_type = None
        self._username = None
        self._password = None
        self._disabled = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if host_address is not None:
            self.host_address = host_address
        if description is not None:
            self.description = description
        if port is not None:
            self.port = port
        if server_type is not None:
            self.server_type = server_type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if disabled is not None:
            self.disabled = disabled

    @property
    def id(self):
        """Gets the id of this ServerJson.  # noqa: E501


        :return: The id of this ServerJson.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerJson.


        :param id: The id of this ServerJson.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def host_address(self):
        """Gets the host_address of this ServerJson.  # noqa: E501


        :return: The host_address of this ServerJson.  # noqa: E501
        :rtype: str
        """
        return self._host_address

    @host_address.setter
    def host_address(self, host_address):
        """Sets the host_address of this ServerJson.


        :param host_address: The host_address of this ServerJson.  # noqa: E501
        :type: str
        """

        self._host_address = host_address

    @property
    def description(self):
        """Gets the description of this ServerJson.  # noqa: E501


        :return: The description of this ServerJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServerJson.


        :param description: The description of this ServerJson.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def port(self):
        """Gets the port of this ServerJson.  # noqa: E501


        :return: The port of this ServerJson.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerJson.


        :param port: The port of this ServerJson.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def server_type(self):
        """Gets the server_type of this ServerJson.  # noqa: E501


        :return: The server_type of this ServerJson.  # noqa: E501
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this ServerJson.


        :param server_type: The server_type of this ServerJson.  # noqa: E501
        :type: str
        """

        self._server_type = server_type

    @property
    def username(self):
        """Gets the username of this ServerJson.  # noqa: E501


        :return: The username of this ServerJson.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ServerJson.


        :param username: The username of this ServerJson.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this ServerJson.  # noqa: E501


        :return: The password of this ServerJson.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ServerJson.


        :param password: The password of this ServerJson.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def disabled(self):
        """Gets the disabled of this ServerJson.  # noqa: E501


        :return: The disabled of this ServerJson.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ServerJson.


        :param disabled: The disabled of this ServerJson.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ServerJson, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
