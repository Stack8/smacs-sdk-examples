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

class CucmLicenseUsageUserJson(object):
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
        'owner_id': 'str',
        'cucm_current_license': 'str',
        'cucm_optimal_license': 'str',
        'devices': 'list[CucmLicenseUsageDeviceJson]'
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'cucm_current_license': 'cucmCurrentLicense',
        'cucm_optimal_license': 'cucmOptimalLicense',
        'devices': 'devices'
    }

    def __init__(self, owner_id=None, cucm_current_license=None, cucm_optimal_license=None, devices=None):  # noqa: E501
        """CucmLicenseUsageUserJson - a model defined in Swagger"""  # noqa: E501
        self._owner_id = None
        self._cucm_current_license = None
        self._cucm_optimal_license = None
        self._devices = None
        self.discriminator = None
        if owner_id is not None:
            self.owner_id = owner_id
        if cucm_current_license is not None:
            self.cucm_current_license = cucm_current_license
        if cucm_optimal_license is not None:
            self.cucm_optimal_license = cucm_optimal_license
        if devices is not None:
            self.devices = devices

    @property
    def owner_id(self):
        """Gets the owner_id of this CucmLicenseUsageUserJson.  # noqa: E501


        :return: The owner_id of this CucmLicenseUsageUserJson.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CucmLicenseUsageUserJson.


        :param owner_id: The owner_id of this CucmLicenseUsageUserJson.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def cucm_current_license(self):
        """Gets the cucm_current_license of this CucmLicenseUsageUserJson.  # noqa: E501


        :return: The cucm_current_license of this CucmLicenseUsageUserJson.  # noqa: E501
        :rtype: str
        """
        return self._cucm_current_license

    @cucm_current_license.setter
    def cucm_current_license(self, cucm_current_license):
        """Sets the cucm_current_license of this CucmLicenseUsageUserJson.


        :param cucm_current_license: The cucm_current_license of this CucmLicenseUsageUserJson.  # noqa: E501
        :type: str
        """

        self._cucm_current_license = cucm_current_license

    @property
    def cucm_optimal_license(self):
        """Gets the cucm_optimal_license of this CucmLicenseUsageUserJson.  # noqa: E501


        :return: The cucm_optimal_license of this CucmLicenseUsageUserJson.  # noqa: E501
        :rtype: str
        """
        return self._cucm_optimal_license

    @cucm_optimal_license.setter
    def cucm_optimal_license(self, cucm_optimal_license):
        """Sets the cucm_optimal_license of this CucmLicenseUsageUserJson.


        :param cucm_optimal_license: The cucm_optimal_license of this CucmLicenseUsageUserJson.  # noqa: E501
        :type: str
        """

        self._cucm_optimal_license = cucm_optimal_license

    @property
    def devices(self):
        """Gets the devices of this CucmLicenseUsageUserJson.  # noqa: E501


        :return: The devices of this CucmLicenseUsageUserJson.  # noqa: E501
        :rtype: list[CucmLicenseUsageDeviceJson]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this CucmLicenseUsageUserJson.


        :param devices: The devices of this CucmLicenseUsageUserJson.  # noqa: E501
        :type: list[CucmLicenseUsageDeviceJson]
        """

        self._devices = devices

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
        if issubclass(CucmLicenseUsageUserJson, dict):
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
        if not isinstance(other, CucmLicenseUsageUserJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
