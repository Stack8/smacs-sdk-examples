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


class DialPlanManagementGroupJson(object):
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
        'id': 'int',
        'name': 'str',
        'site_ids': 'list[int]',
        'cluster_id': 'int',
        'directory_number_ranges_section': 'DirectoryNumberRangesSectionJson',
        'write_ldap_section': 'WriteLdapSectionJson',
        'translation_pattern_ranges_section': 'TranslationPatternRangesSectionJson',
        'enterprise_alternate_number_section': 'IlsAlternateNumberSectionJson',
        'e164_alternate_number_section': 'IlsAlternateNumberSectionJson',
        'pstn_failover_section': 'PstnFailoverSectionJson'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'site_ids': 'siteIds',
        'cluster_id': 'clusterId',
        'directory_number_ranges_section': 'directoryNumberRangesSection',
        'write_ldap_section': 'writeLdapSection',
        'translation_pattern_ranges_section': 'translationPatternRangesSection',
        'enterprise_alternate_number_section': 'enterpriseAlternateNumberSection',
        'e164_alternate_number_section': 'e164AlternateNumberSection',
        'pstn_failover_section': 'pstnFailoverSection'
    }

    def __init__(self, id=None, name=None, site_ids=None, cluster_id=None, directory_number_ranges_section=None, write_ldap_section=None, translation_pattern_ranges_section=None, enterprise_alternate_number_section=None, e164_alternate_number_section=None, pstn_failover_section=None):  # noqa: E501
        """DialPlanManagementGroupJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._site_ids = None
        self._cluster_id = None
        self._directory_number_ranges_section = None
        self._write_ldap_section = None
        self._translation_pattern_ranges_section = None
        self._enterprise_alternate_number_section = None
        self._e164_alternate_number_section = None
        self._pstn_failover_section = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if site_ids is not None:
            self.site_ids = site_ids
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if directory_number_ranges_section is not None:
            self.directory_number_ranges_section = directory_number_ranges_section
        if write_ldap_section is not None:
            self.write_ldap_section = write_ldap_section
        if translation_pattern_ranges_section is not None:
            self.translation_pattern_ranges_section = translation_pattern_ranges_section
        if enterprise_alternate_number_section is not None:
            self.enterprise_alternate_number_section = enterprise_alternate_number_section
        if e164_alternate_number_section is not None:
            self.e164_alternate_number_section = e164_alternate_number_section
        if pstn_failover_section is not None:
            self.pstn_failover_section = pstn_failover_section

    @property
    def id(self):
        """Gets the id of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The id of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DialPlanManagementGroupJson.


        :param id: The id of this DialPlanManagementGroupJson.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The name of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DialPlanManagementGroupJson.


        :param name: The name of this DialPlanManagementGroupJson.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def site_ids(self):
        """Gets the site_ids of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The site_ids of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: list[int]
        """
        return self._site_ids

    @site_ids.setter
    def site_ids(self, site_ids):
        """Sets the site_ids of this DialPlanManagementGroupJson.


        :param site_ids: The site_ids of this DialPlanManagementGroupJson.  # noqa: E501
        :type: list[int]
        """

        self._site_ids = site_ids

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The cluster_id of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DialPlanManagementGroupJson.


        :param cluster_id: The cluster_id of this DialPlanManagementGroupJson.  # noqa: E501
        :type: int
        """

        self._cluster_id = cluster_id

    @property
    def directory_number_ranges_section(self):
        """Gets the directory_number_ranges_section of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The directory_number_ranges_section of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: DirectoryNumberRangesSectionJson
        """
        return self._directory_number_ranges_section

    @directory_number_ranges_section.setter
    def directory_number_ranges_section(self, directory_number_ranges_section):
        """Sets the directory_number_ranges_section of this DialPlanManagementGroupJson.


        :param directory_number_ranges_section: The directory_number_ranges_section of this DialPlanManagementGroupJson.  # noqa: E501
        :type: DirectoryNumberRangesSectionJson
        """

        self._directory_number_ranges_section = directory_number_ranges_section

    @property
    def write_ldap_section(self):
        """Gets the write_ldap_section of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The write_ldap_section of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: WriteLdapSectionJson
        """
        return self._write_ldap_section

    @write_ldap_section.setter
    def write_ldap_section(self, write_ldap_section):
        """Sets the write_ldap_section of this DialPlanManagementGroupJson.


        :param write_ldap_section: The write_ldap_section of this DialPlanManagementGroupJson.  # noqa: E501
        :type: WriteLdapSectionJson
        """

        self._write_ldap_section = write_ldap_section

    @property
    def translation_pattern_ranges_section(self):
        """Gets the translation_pattern_ranges_section of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The translation_pattern_ranges_section of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: TranslationPatternRangesSectionJson
        """
        return self._translation_pattern_ranges_section

    @translation_pattern_ranges_section.setter
    def translation_pattern_ranges_section(self, translation_pattern_ranges_section):
        """Sets the translation_pattern_ranges_section of this DialPlanManagementGroupJson.


        :param translation_pattern_ranges_section: The translation_pattern_ranges_section of this DialPlanManagementGroupJson.  # noqa: E501
        :type: TranslationPatternRangesSectionJson
        """

        self._translation_pattern_ranges_section = translation_pattern_ranges_section

    @property
    def enterprise_alternate_number_section(self):
        """Gets the enterprise_alternate_number_section of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The enterprise_alternate_number_section of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: IlsAlternateNumberSectionJson
        """
        return self._enterprise_alternate_number_section

    @enterprise_alternate_number_section.setter
    def enterprise_alternate_number_section(self, enterprise_alternate_number_section):
        """Sets the enterprise_alternate_number_section of this DialPlanManagementGroupJson.


        :param enterprise_alternate_number_section: The enterprise_alternate_number_section of this DialPlanManagementGroupJson.  # noqa: E501
        :type: IlsAlternateNumberSectionJson
        """

        self._enterprise_alternate_number_section = enterprise_alternate_number_section

    @property
    def e164_alternate_number_section(self):
        """Gets the e164_alternate_number_section of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The e164_alternate_number_section of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: IlsAlternateNumberSectionJson
        """
        return self._e164_alternate_number_section

    @e164_alternate_number_section.setter
    def e164_alternate_number_section(self, e164_alternate_number_section):
        """Sets the e164_alternate_number_section of this DialPlanManagementGroupJson.


        :param e164_alternate_number_section: The e164_alternate_number_section of this DialPlanManagementGroupJson.  # noqa: E501
        :type: IlsAlternateNumberSectionJson
        """

        self._e164_alternate_number_section = e164_alternate_number_section

    @property
    def pstn_failover_section(self):
        """Gets the pstn_failover_section of this DialPlanManagementGroupJson.  # noqa: E501


        :return: The pstn_failover_section of this DialPlanManagementGroupJson.  # noqa: E501
        :rtype: PstnFailoverSectionJson
        """
        return self._pstn_failover_section

    @pstn_failover_section.setter
    def pstn_failover_section(self, pstn_failover_section):
        """Sets the pstn_failover_section of this DialPlanManagementGroupJson.


        :param pstn_failover_section: The pstn_failover_section of this DialPlanManagementGroupJson.  # noqa: E501
        :type: PstnFailoverSectionJson
        """

        self._pstn_failover_section = pstn_failover_section

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
        if issubclass(DialPlanManagementGroupJson, dict):
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
        if not isinstance(other, DialPlanManagementGroupJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
