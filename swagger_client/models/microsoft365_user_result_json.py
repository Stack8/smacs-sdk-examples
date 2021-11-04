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

class Microsoft365UserResultJson(object):
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
        'microsoft365_user_ref': 'Microsoft365UserRefJson'
    }

    attribute_map = {
        'microsoft365_user_ref': 'microsoft365UserRef'
    }

    def __init__(self, microsoft365_user_ref=None):  # noqa: E501
        """Microsoft365UserResultJson - a model defined in Swagger"""  # noqa: E501
        self._microsoft365_user_ref = None
        self.discriminator = None
        self.microsoft365_user_ref = microsoft365_user_ref

    @property
    def microsoft365_user_ref(self):
        """Gets the microsoft365_user_ref of this Microsoft365UserResultJson.  # noqa: E501


        :return: The microsoft365_user_ref of this Microsoft365UserResultJson.  # noqa: E501
        :rtype: Microsoft365UserRefJson
        """
        return self._microsoft365_user_ref

    @microsoft365_user_ref.setter
    def microsoft365_user_ref(self, microsoft365_user_ref):
        """Sets the microsoft365_user_ref of this Microsoft365UserResultJson.


        :param microsoft365_user_ref: The microsoft365_user_ref of this Microsoft365UserResultJson.  # noqa: E501
        :type: Microsoft365UserRefJson
        """
        if microsoft365_user_ref is None:
            raise ValueError("Invalid value for `microsoft365_user_ref`, must not be `None`")  # noqa: E501

        self._microsoft365_user_ref = microsoft365_user_ref

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
        if issubclass(Microsoft365UserResultJson, dict):
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
        if not isinstance(other, Microsoft365UserResultJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
