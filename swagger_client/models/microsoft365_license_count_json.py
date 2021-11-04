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

class Microsoft365LicenseCountJson(object):
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
        'microsoft365_license_json': 'Microsoft365LicenseJson',
        'total': 'int',
        'consumed': 'int',
        'available': 'int'
    }

    attribute_map = {
        'microsoft365_license_json': 'microsoft365LicenseJson',
        'total': 'total',
        'consumed': 'consumed',
        'available': 'available'
    }

    def __init__(self, microsoft365_license_json=None, total=None, consumed=None, available=None):  # noqa: E501
        """Microsoft365LicenseCountJson - a model defined in Swagger"""  # noqa: E501
        self._microsoft365_license_json = None
        self._total = None
        self._consumed = None
        self._available = None
        self.discriminator = None
        if microsoft365_license_json is not None:
            self.microsoft365_license_json = microsoft365_license_json
        if total is not None:
            self.total = total
        if consumed is not None:
            self.consumed = consumed
        if available is not None:
            self.available = available

    @property
    def microsoft365_license_json(self):
        """Gets the microsoft365_license_json of this Microsoft365LicenseCountJson.  # noqa: E501


        :return: The microsoft365_license_json of this Microsoft365LicenseCountJson.  # noqa: E501
        :rtype: Microsoft365LicenseJson
        """
        return self._microsoft365_license_json

    @microsoft365_license_json.setter
    def microsoft365_license_json(self, microsoft365_license_json):
        """Sets the microsoft365_license_json of this Microsoft365LicenseCountJson.


        :param microsoft365_license_json: The microsoft365_license_json of this Microsoft365LicenseCountJson.  # noqa: E501
        :type: Microsoft365LicenseJson
        """

        self._microsoft365_license_json = microsoft365_license_json

    @property
    def total(self):
        """Gets the total of this Microsoft365LicenseCountJson.  # noqa: E501


        :return: The total of this Microsoft365LicenseCountJson.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Microsoft365LicenseCountJson.


        :param total: The total of this Microsoft365LicenseCountJson.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def consumed(self):
        """Gets the consumed of this Microsoft365LicenseCountJson.  # noqa: E501


        :return: The consumed of this Microsoft365LicenseCountJson.  # noqa: E501
        :rtype: int
        """
        return self._consumed

    @consumed.setter
    def consumed(self, consumed):
        """Sets the consumed of this Microsoft365LicenseCountJson.


        :param consumed: The consumed of this Microsoft365LicenseCountJson.  # noqa: E501
        :type: int
        """

        self._consumed = consumed

    @property
    def available(self):
        """Gets the available of this Microsoft365LicenseCountJson.  # noqa: E501


        :return: The available of this Microsoft365LicenseCountJson.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this Microsoft365LicenseCountJson.


        :param available: The available of this Microsoft365LicenseCountJson.  # noqa: E501
        :type: int
        """

        self._available = available

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
        if issubclass(Microsoft365LicenseCountJson, dict):
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
        if not isinstance(other, Microsoft365LicenseCountJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other