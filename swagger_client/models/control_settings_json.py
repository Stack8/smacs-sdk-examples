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

class ControlSettingsJson(object):
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
        'cdr_file_processing_frequency_in_minutes': 'int',
        'utilization_processing_frequency_in_minutes': 'int',
        'cdr_retention_in_days': 'int',
        'new_device_max_age_in_days': 'int',
        'cdr_clean_up_frequency_in_minutes': 'int'
    }

    attribute_map = {
        'cdr_file_processing_frequency_in_minutes': 'cdrFileProcessingFrequencyInMinutes',
        'utilization_processing_frequency_in_minutes': 'utilizationProcessingFrequencyInMinutes',
        'cdr_retention_in_days': 'cdrRetentionInDays',
        'new_device_max_age_in_days': 'newDeviceMaxAgeInDays',
        'cdr_clean_up_frequency_in_minutes': 'cdrCleanUpFrequencyInMinutes'
    }

    def __init__(self, cdr_file_processing_frequency_in_minutes=None, utilization_processing_frequency_in_minutes=None, cdr_retention_in_days=None, new_device_max_age_in_days=None, cdr_clean_up_frequency_in_minutes=None):  # noqa: E501
        """ControlSettingsJson - a model defined in Swagger"""  # noqa: E501
        self._cdr_file_processing_frequency_in_minutes = None
        self._utilization_processing_frequency_in_minutes = None
        self._cdr_retention_in_days = None
        self._new_device_max_age_in_days = None
        self._cdr_clean_up_frequency_in_minutes = None
        self.discriminator = None
        self.cdr_file_processing_frequency_in_minutes = cdr_file_processing_frequency_in_minutes
        self.utilization_processing_frequency_in_minutes = utilization_processing_frequency_in_minutes
        self.cdr_retention_in_days = cdr_retention_in_days
        self.new_device_max_age_in_days = new_device_max_age_in_days
        self.cdr_clean_up_frequency_in_minutes = cdr_clean_up_frequency_in_minutes

    @property
    def cdr_file_processing_frequency_in_minutes(self):
        """Gets the cdr_file_processing_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501


        :return: The cdr_file_processing_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501
        :rtype: int
        """
        return self._cdr_file_processing_frequency_in_minutes

    @cdr_file_processing_frequency_in_minutes.setter
    def cdr_file_processing_frequency_in_minutes(self, cdr_file_processing_frequency_in_minutes):
        """Sets the cdr_file_processing_frequency_in_minutes of this ControlSettingsJson.


        :param cdr_file_processing_frequency_in_minutes: The cdr_file_processing_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501
        :type: int
        """
        if cdr_file_processing_frequency_in_minutes is None:
            raise ValueError("Invalid value for `cdr_file_processing_frequency_in_minutes`, must not be `None`")  # noqa: E501

        self._cdr_file_processing_frequency_in_minutes = cdr_file_processing_frequency_in_minutes

    @property
    def utilization_processing_frequency_in_minutes(self):
        """Gets the utilization_processing_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501


        :return: The utilization_processing_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501
        :rtype: int
        """
        return self._utilization_processing_frequency_in_minutes

    @utilization_processing_frequency_in_minutes.setter
    def utilization_processing_frequency_in_minutes(self, utilization_processing_frequency_in_minutes):
        """Sets the utilization_processing_frequency_in_minutes of this ControlSettingsJson.


        :param utilization_processing_frequency_in_minutes: The utilization_processing_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501
        :type: int
        """
        if utilization_processing_frequency_in_minutes is None:
            raise ValueError("Invalid value for `utilization_processing_frequency_in_minutes`, must not be `None`")  # noqa: E501

        self._utilization_processing_frequency_in_minutes = utilization_processing_frequency_in_minutes

    @property
    def cdr_retention_in_days(self):
        """Gets the cdr_retention_in_days of this ControlSettingsJson.  # noqa: E501


        :return: The cdr_retention_in_days of this ControlSettingsJson.  # noqa: E501
        :rtype: int
        """
        return self._cdr_retention_in_days

    @cdr_retention_in_days.setter
    def cdr_retention_in_days(self, cdr_retention_in_days):
        """Sets the cdr_retention_in_days of this ControlSettingsJson.


        :param cdr_retention_in_days: The cdr_retention_in_days of this ControlSettingsJson.  # noqa: E501
        :type: int
        """
        if cdr_retention_in_days is None:
            raise ValueError("Invalid value for `cdr_retention_in_days`, must not be `None`")  # noqa: E501

        self._cdr_retention_in_days = cdr_retention_in_days

    @property
    def new_device_max_age_in_days(self):
        """Gets the new_device_max_age_in_days of this ControlSettingsJson.  # noqa: E501


        :return: The new_device_max_age_in_days of this ControlSettingsJson.  # noqa: E501
        :rtype: int
        """
        return self._new_device_max_age_in_days

    @new_device_max_age_in_days.setter
    def new_device_max_age_in_days(self, new_device_max_age_in_days):
        """Sets the new_device_max_age_in_days of this ControlSettingsJson.


        :param new_device_max_age_in_days: The new_device_max_age_in_days of this ControlSettingsJson.  # noqa: E501
        :type: int
        """
        if new_device_max_age_in_days is None:
            raise ValueError("Invalid value for `new_device_max_age_in_days`, must not be `None`")  # noqa: E501

        self._new_device_max_age_in_days = new_device_max_age_in_days

    @property
    def cdr_clean_up_frequency_in_minutes(self):
        """Gets the cdr_clean_up_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501


        :return: The cdr_clean_up_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501
        :rtype: int
        """
        return self._cdr_clean_up_frequency_in_minutes

    @cdr_clean_up_frequency_in_minutes.setter
    def cdr_clean_up_frequency_in_minutes(self, cdr_clean_up_frequency_in_minutes):
        """Sets the cdr_clean_up_frequency_in_minutes of this ControlSettingsJson.


        :param cdr_clean_up_frequency_in_minutes: The cdr_clean_up_frequency_in_minutes of this ControlSettingsJson.  # noqa: E501
        :type: int
        """
        if cdr_clean_up_frequency_in_minutes is None:
            raise ValueError("Invalid value for `cdr_clean_up_frequency_in_minutes`, must not be `None`")  # noqa: E501

        self._cdr_clean_up_frequency_in_minutes = cdr_clean_up_frequency_in_minutes

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
        if issubclass(ControlSettingsJson, dict):
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
        if not isinstance(other, ControlSettingsJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
