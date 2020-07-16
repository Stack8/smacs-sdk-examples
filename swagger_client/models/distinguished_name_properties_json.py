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


class DistinguishedNamePropertiesJson(object):
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
        'country': 'str',
        'state': 'str',
        'locality': 'str',
        'organization': 'str',
        'organizational_unit': 'str',
        'common_name': 'str',
        'subject_alternative_names': 'list[str]'
    }

    attribute_map = {
        'country': 'country',
        'state': 'state',
        'locality': 'locality',
        'organization': 'organization',
        'organizational_unit': 'organizationalUnit',
        'common_name': 'commonName',
        'subject_alternative_names': 'subjectAlternativeNames'
    }

    def __init__(self, country=None, state=None, locality=None, organization=None, organizational_unit=None, common_name=None, subject_alternative_names=None):  # noqa: E501
        """DistinguishedNamePropertiesJson - a model defined in Swagger"""  # noqa: E501
        self._country = None
        self._state = None
        self._locality = None
        self._organization = None
        self._organizational_unit = None
        self._common_name = None
        self._subject_alternative_names = None
        self.discriminator = None
        if country is not None:
            self.country = country
        if state is not None:
            self.state = state
        if locality is not None:
            self.locality = locality
        if organization is not None:
            self.organization = organization
        if organizational_unit is not None:
            self.organizational_unit = organizational_unit
        if common_name is not None:
            self.common_name = common_name
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names

    @property
    def country(self):
        """Gets the country of this DistinguishedNamePropertiesJson.  # noqa: E501


        :return: The country of this DistinguishedNamePropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this DistinguishedNamePropertiesJson.


        :param country: The country of this DistinguishedNamePropertiesJson.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this DistinguishedNamePropertiesJson.  # noqa: E501


        :return: The state of this DistinguishedNamePropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DistinguishedNamePropertiesJson.


        :param state: The state of this DistinguishedNamePropertiesJson.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def locality(self):
        """Gets the locality of this DistinguishedNamePropertiesJson.  # noqa: E501


        :return: The locality of this DistinguishedNamePropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this DistinguishedNamePropertiesJson.


        :param locality: The locality of this DistinguishedNamePropertiesJson.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def organization(self):
        """Gets the organization of this DistinguishedNamePropertiesJson.  # noqa: E501


        :return: The organization of this DistinguishedNamePropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this DistinguishedNamePropertiesJson.


        :param organization: The organization of this DistinguishedNamePropertiesJson.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def organizational_unit(self):
        """Gets the organizational_unit of this DistinguishedNamePropertiesJson.  # noqa: E501


        :return: The organizational_unit of this DistinguishedNamePropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """Sets the organizational_unit of this DistinguishedNamePropertiesJson.


        :param organizational_unit: The organizational_unit of this DistinguishedNamePropertiesJson.  # noqa: E501
        :type: str
        """

        self._organizational_unit = organizational_unit

    @property
    def common_name(self):
        """Gets the common_name of this DistinguishedNamePropertiesJson.  # noqa: E501


        :return: The common_name of this DistinguishedNamePropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this DistinguishedNamePropertiesJson.


        :param common_name: The common_name of this DistinguishedNamePropertiesJson.  # noqa: E501
        :type: str
        """

        self._common_name = common_name

    @property
    def subject_alternative_names(self):
        """Gets the subject_alternative_names of this DistinguishedNamePropertiesJson.  # noqa: E501


        :return: The subject_alternative_names of this DistinguishedNamePropertiesJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """Sets the subject_alternative_names of this DistinguishedNamePropertiesJson.


        :param subject_alternative_names: The subject_alternative_names of this DistinguishedNamePropertiesJson.  # noqa: E501
        :type: list[str]
        """

        self._subject_alternative_names = subject_alternative_names

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
        if issubclass(DistinguishedNamePropertiesJson, dict):
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
        if not isinstance(other, DistinguishedNamePropertiesJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
