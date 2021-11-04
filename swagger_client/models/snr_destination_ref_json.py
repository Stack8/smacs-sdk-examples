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

class SnrDestinationRefJson(object):
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
        'id': 'str',
        'server_id': 'int',
        'url': 'str',
        'name': 'str',
        'destination': 'str'
    }

    attribute_map = {
        'id': 'id',
        'server_id': 'serverId',
        'url': 'url',
        'name': 'name',
        'destination': 'destination'
    }

    def __init__(self, id=None, server_id=None, url=None, name=None, destination=None):  # noqa: E501
        """SnrDestinationRefJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._server_id = None
        self._url = None
        self._name = None
        self._destination = None
        self.discriminator = None
        self.id = id
        if server_id is not None:
            self.server_id = server_id
        if url is not None:
            self.url = url
        if name is not None:
            self.name = name
        if destination is not None:
            self.destination = destination

    @property
    def id(self):
        """Gets the id of this SnrDestinationRefJson.  # noqa: E501


        :return: The id of this SnrDestinationRefJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnrDestinationRefJson.


        :param id: The id of this SnrDestinationRefJson.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this SnrDestinationRefJson.  # noqa: E501


        :return: The server_id of this SnrDestinationRefJson.  # noqa: E501
        :rtype: int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this SnrDestinationRefJson.


        :param server_id: The server_id of this SnrDestinationRefJson.  # noqa: E501
        :type: int
        """

        self._server_id = server_id

    @property
    def url(self):
        """Gets the url of this SnrDestinationRefJson.  # noqa: E501


        :return: The url of this SnrDestinationRefJson.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SnrDestinationRefJson.


        :param url: The url of this SnrDestinationRefJson.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this SnrDestinationRefJson.  # noqa: E501


        :return: The name of this SnrDestinationRefJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnrDestinationRefJson.


        :param name: The name of this SnrDestinationRefJson.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def destination(self):
        """Gets the destination of this SnrDestinationRefJson.  # noqa: E501


        :return: The destination of this SnrDestinationRefJson.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this SnrDestinationRefJson.


        :param destination: The destination of this SnrDestinationRefJson.  # noqa: E501
        :type: str
        """

        self._destination = destination

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
        if issubclass(SnrDestinationRefJson, dict):
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
        if not isinstance(other, SnrDestinationRefJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
