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

class LdapUserDialPlanDetailsFieldConfigJson(object):
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
        'e164_number': 'TextFieldConfigJson',
        'extension': 'TextFieldConfigJson'
    }

    attribute_map = {
        'e164_number': 'e164Number',
        'extension': 'extension'
    }

    def __init__(self, e164_number=None, extension=None):  # noqa: E501
        """LdapUserDialPlanDetailsFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._e164_number = None
        self._extension = None
        self.discriminator = None
        if e164_number is not None:
            self.e164_number = e164_number
        if extension is not None:
            self.extension = extension

    @property
    def e164_number(self):
        """Gets the e164_number of this LdapUserDialPlanDetailsFieldConfigJson.  # noqa: E501


        :return: The e164_number of this LdapUserDialPlanDetailsFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._e164_number

    @e164_number.setter
    def e164_number(self, e164_number):
        """Sets the e164_number of this LdapUserDialPlanDetailsFieldConfigJson.


        :param e164_number: The e164_number of this LdapUserDialPlanDetailsFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """

        self._e164_number = e164_number

    @property
    def extension(self):
        """Gets the extension of this LdapUserDialPlanDetailsFieldConfigJson.  # noqa: E501


        :return: The extension of this LdapUserDialPlanDetailsFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this LdapUserDialPlanDetailsFieldConfigJson.


        :param extension: The extension of this LdapUserDialPlanDetailsFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
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
        if issubclass(LdapUserDialPlanDetailsFieldConfigJson, dict):
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
        if not isinstance(other, LdapUserDialPlanDetailsFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other