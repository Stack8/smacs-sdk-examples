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

class CustomMultiSelectEndUserRefFieldConfigJson(object):
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
        'show': 'bool',
        'required': 'bool',
        'default_values': 'list[EndUserRefJson]',
        'possible_options': 'list[EndUserRefJson]'
    }

    attribute_map = {
        'show': 'show',
        'required': 'required',
        'default_values': 'defaultValues',
        'possible_options': 'possibleOptions'
    }

    def __init__(self, show=None, required=None, default_values=None, possible_options=None):  # noqa: E501
        """CustomMultiSelectEndUserRefFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._show = None
        self._required = None
        self._default_values = None
        self._possible_options = None
        self.discriminator = None
        if show is not None:
            self.show = show
        if required is not None:
            self.required = required
        if default_values is not None:
            self.default_values = default_values
        if possible_options is not None:
            self.possible_options = possible_options

    @property
    def show(self):
        """Gets the show of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501


        :return: The show of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :rtype: bool
        """
        return self._show

    @show.setter
    def show(self, show):
        """Sets the show of this CustomMultiSelectEndUserRefFieldConfigJson.


        :param show: The show of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :type: bool
        """

        self._show = show

    @property
    def required(self):
        """Gets the required of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501


        :return: The required of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CustomMultiSelectEndUserRefFieldConfigJson.


        :param required: The required of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def default_values(self):
        """Gets the default_values of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501


        :return: The default_values of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :rtype: list[EndUserRefJson]
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this CustomMultiSelectEndUserRefFieldConfigJson.


        :param default_values: The default_values of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :type: list[EndUserRefJson]
        """

        self._default_values = default_values

    @property
    def possible_options(self):
        """Gets the possible_options of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501


        :return: The possible_options of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :rtype: list[EndUserRefJson]
        """
        return self._possible_options

    @possible_options.setter
    def possible_options(self, possible_options):
        """Sets the possible_options of this CustomMultiSelectEndUserRefFieldConfigJson.


        :param possible_options: The possible_options of this CustomMultiSelectEndUserRefFieldConfigJson.  # noqa: E501
        :type: list[EndUserRefJson]
        """

        self._possible_options = possible_options

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
        if issubclass(CustomMultiSelectEndUserRefFieldConfigJson, dict):
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
        if not isinstance(other, CustomMultiSelectEndUserRefFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
