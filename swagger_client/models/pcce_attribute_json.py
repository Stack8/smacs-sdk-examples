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

class PcceAttributeJson(object):
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
        'type': 'str',
        'name': 'str',
        'ref_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'ref_url': 'refUrl'
    }

    def __init__(self, type=None, name=None, ref_url=None):  # noqa: E501
        """PcceAttributeJson - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._ref_url = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if ref_url is not None:
            self.ref_url = ref_url

    @property
    def type(self):
        """Gets the type of this PcceAttributeJson.  # noqa: E501


        :return: The type of this PcceAttributeJson.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PcceAttributeJson.


        :param type: The type of this PcceAttributeJson.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this PcceAttributeJson.  # noqa: E501


        :return: The name of this PcceAttributeJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PcceAttributeJson.


        :param name: The name of this PcceAttributeJson.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ref_url(self):
        """Gets the ref_url of this PcceAttributeJson.  # noqa: E501


        :return: The ref_url of this PcceAttributeJson.  # noqa: E501
        :rtype: str
        """
        return self._ref_url

    @ref_url.setter
    def ref_url(self, ref_url):
        """Sets the ref_url of this PcceAttributeJson.


        :param ref_url: The ref_url of this PcceAttributeJson.  # noqa: E501
        :type: str
        """

        self._ref_url = ref_url

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
        if issubclass(PcceAttributeJson, dict):
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
        if not isinstance(other, PcceAttributeJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
