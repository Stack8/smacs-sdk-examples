# coding: utf-8

"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PhoneServiceParameterMetadataJson(object):
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
        'name': 'str',
        'default_value': 'str',
        'display_name': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'default_value': 'defaultValue',
        'display_name': 'displayName',
        'required': 'required'
    }

    def __init__(self, name=None, default_value=None, display_name=None, required=None):  # noqa: E501
        """PhoneServiceParameterMetadataJson - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._default_value = None
        self._display_name = None
        self._required = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if default_value is not None:
            self.default_value = default_value
        if display_name is not None:
            self.display_name = display_name
        if required is not None:
            self.required = required

    @property
    def name(self):
        """Gets the name of this PhoneServiceParameterMetadataJson.  # noqa: E501


        :return: The name of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhoneServiceParameterMetadataJson.


        :param name: The name of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def default_value(self):
        """Gets the default_value of this PhoneServiceParameterMetadataJson.  # noqa: E501


        :return: The default_value of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this PhoneServiceParameterMetadataJson.


        :param default_value: The default_value of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def display_name(self):
        """Gets the display_name of this PhoneServiceParameterMetadataJson.  # noqa: E501


        :return: The display_name of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PhoneServiceParameterMetadataJson.


        :param display_name: The display_name of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def required(self):
        """Gets the required of this PhoneServiceParameterMetadataJson.  # noqa: E501


        :return: The required of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this PhoneServiceParameterMetadataJson.


        :param required: The required of this PhoneServiceParameterMetadataJson.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(PhoneServiceParameterMetadataJson, dict):
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
        if not isinstance(other, PhoneServiceParameterMetadataJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
