# coding: utf-8

"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PcceMetadataJson(object):
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
        'description': 'str',
        'version': 'str',
        'departments': 'list[PcceDepartmentJson]',
        'desk_settings': 'list[PcceRefJson]',
        'teams': 'list[PcceRefJson]',
        'attributes': 'list[PcceRefJson]',
        'skill_groups': 'list[PcceRefJson]'
    }

    attribute_map = {
        'description': 'description',
        'version': 'version',
        'departments': 'departments',
        'desk_settings': 'deskSettings',
        'teams': 'teams',
        'attributes': 'attributes',
        'skill_groups': 'skillGroups'
    }

    def __init__(self, description=None, version=None, departments=None, desk_settings=None, teams=None, attributes=None, skill_groups=None):  # noqa: E501
        """PcceMetadataJson - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._version = None
        self._departments = None
        self._desk_settings = None
        self._teams = None
        self._attributes = None
        self._skill_groups = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if departments is not None:
            self.departments = departments
        if desk_settings is not None:
            self.desk_settings = desk_settings
        if teams is not None:
            self.teams = teams
        if attributes is not None:
            self.attributes = attributes
        if skill_groups is not None:
            self.skill_groups = skill_groups

    @property
    def description(self):
        """Gets the description of this PcceMetadataJson.  # noqa: E501


        :return: The description of this PcceMetadataJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PcceMetadataJson.


        :param description: The description of this PcceMetadataJson.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this PcceMetadataJson.  # noqa: E501


        :return: The version of this PcceMetadataJson.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PcceMetadataJson.


        :param version: The version of this PcceMetadataJson.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def departments(self):
        """Gets the departments of this PcceMetadataJson.  # noqa: E501


        :return: The departments of this PcceMetadataJson.  # noqa: E501
        :rtype: list[PcceDepartmentJson]
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """Sets the departments of this PcceMetadataJson.


        :param departments: The departments of this PcceMetadataJson.  # noqa: E501
        :type: list[PcceDepartmentJson]
        """

        self._departments = departments

    @property
    def desk_settings(self):
        """Gets the desk_settings of this PcceMetadataJson.  # noqa: E501


        :return: The desk_settings of this PcceMetadataJson.  # noqa: E501
        :rtype: list[PcceRefJson]
        """
        return self._desk_settings

    @desk_settings.setter
    def desk_settings(self, desk_settings):
        """Sets the desk_settings of this PcceMetadataJson.


        :param desk_settings: The desk_settings of this PcceMetadataJson.  # noqa: E501
        :type: list[PcceRefJson]
        """

        self._desk_settings = desk_settings

    @property
    def teams(self):
        """Gets the teams of this PcceMetadataJson.  # noqa: E501


        :return: The teams of this PcceMetadataJson.  # noqa: E501
        :rtype: list[PcceRefJson]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this PcceMetadataJson.


        :param teams: The teams of this PcceMetadataJson.  # noqa: E501
        :type: list[PcceRefJson]
        """

        self._teams = teams

    @property
    def attributes(self):
        """Gets the attributes of this PcceMetadataJson.  # noqa: E501


        :return: The attributes of this PcceMetadataJson.  # noqa: E501
        :rtype: list[PcceRefJson]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this PcceMetadataJson.


        :param attributes: The attributes of this PcceMetadataJson.  # noqa: E501
        :type: list[PcceRefJson]
        """

        self._attributes = attributes

    @property
    def skill_groups(self):
        """Gets the skill_groups of this PcceMetadataJson.  # noqa: E501


        :return: The skill_groups of this PcceMetadataJson.  # noqa: E501
        :rtype: list[PcceRefJson]
        """
        return self._skill_groups

    @skill_groups.setter
    def skill_groups(self, skill_groups):
        """Sets the skill_groups of this PcceMetadataJson.


        :param skill_groups: The skill_groups of this PcceMetadataJson.  # noqa: E501
        :type: list[PcceRefJson]
        """

        self._skill_groups = skill_groups

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
        if issubclass(PcceMetadataJson, dict):
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
        if not isinstance(other, PcceMetadataJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
