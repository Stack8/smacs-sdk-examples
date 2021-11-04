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

class DistributionListResultJson(object):
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
        'ref': 'DistributionListRefJson',
        'alias': 'str',
        'display_name': 'str',
        'extension': 'str'
    }

    attribute_map = {
        'ref': 'ref',
        'alias': 'alias',
        'display_name': 'displayName',
        'extension': 'extension'
    }

    def __init__(self, ref=None, alias=None, display_name=None, extension=None):  # noqa: E501
        """DistributionListResultJson - a model defined in Swagger"""  # noqa: E501
        self._ref = None
        self._alias = None
        self._display_name = None
        self._extension = None
        self.discriminator = None
        if ref is not None:
            self.ref = ref
        if alias is not None:
            self.alias = alias
        if display_name is not None:
            self.display_name = display_name
        if extension is not None:
            self.extension = extension

    @property
    def ref(self):
        """Gets the ref of this DistributionListResultJson.  # noqa: E501


        :return: The ref of this DistributionListResultJson.  # noqa: E501
        :rtype: DistributionListRefJson
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this DistributionListResultJson.


        :param ref: The ref of this DistributionListResultJson.  # noqa: E501
        :type: DistributionListRefJson
        """

        self._ref = ref

    @property
    def alias(self):
        """Gets the alias of this DistributionListResultJson.  # noqa: E501


        :return: The alias of this DistributionListResultJson.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DistributionListResultJson.


        :param alias: The alias of this DistributionListResultJson.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def display_name(self):
        """Gets the display_name of this DistributionListResultJson.  # noqa: E501


        :return: The display_name of this DistributionListResultJson.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DistributionListResultJson.


        :param display_name: The display_name of this DistributionListResultJson.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def extension(self):
        """Gets the extension of this DistributionListResultJson.  # noqa: E501


        :return: The extension of this DistributionListResultJson.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this DistributionListResultJson.


        :param extension: The extension of this DistributionListResultJson.  # noqa: E501
        :type: str
        """

        self._extension = extension

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
        if issubclass(DistributionListResultJson, dict):
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
        if not isinstance(other, DistributionListResultJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
