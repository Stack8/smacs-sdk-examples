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

class LineButtonJson(object):
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
        'dn': 'DirectoryNumberRefJson',
        'line_feature': 'LineFeatureJson'
    }

    attribute_map = {
        'type': 'type',
        'dn': 'dn',
        'line_feature': 'lineFeature'
    }

    def __init__(self, type=None, dn=None, line_feature=None):  # noqa: E501
        """LineButtonJson - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._dn = None
        self._line_feature = None
        self.discriminator = None
        self.type = type
        if dn is not None:
            self.dn = dn
        if line_feature is not None:
            self.line_feature = line_feature

    @property
    def type(self):
        """Gets the type of this LineButtonJson.  # noqa: E501


        :return: The type of this LineButtonJson.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LineButtonJson.


        :param type: The type of this LineButtonJson.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def dn(self):
        """Gets the dn of this LineButtonJson.  # noqa: E501


        :return: The dn of this LineButtonJson.  # noqa: E501
        :rtype: DirectoryNumberRefJson
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this LineButtonJson.


        :param dn: The dn of this LineButtonJson.  # noqa: E501
        :type: DirectoryNumberRefJson
        """

        self._dn = dn

    @property
    def line_feature(self):
        """Gets the line_feature of this LineButtonJson.  # noqa: E501


        :return: The line_feature of this LineButtonJson.  # noqa: E501
        :rtype: LineFeatureJson
        """
        return self._line_feature

    @line_feature.setter
    def line_feature(self, line_feature):
        """Sets the line_feature of this LineButtonJson.


        :param line_feature: The line_feature of this LineButtonJson.  # noqa: E501
        :type: LineFeatureJson
        """

        self._line_feature = line_feature

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
        if issubclass(LineButtonJson, dict):
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
        if not isinstance(other, LineButtonJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
