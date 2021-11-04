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

class PcceAgentsFieldConfigJson(object):
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
        'departments': 'SelectFieldConfigJson',
        'teams': 'SelectFieldConfigJson',
        'desk_settings': 'SelectFieldConfigJson',
        'skill_groups': 'SelectFieldConfigJson',
        'boolean_attributes': 'list[str]',
        'proficiency_attributes': 'list[str]'
    }

    attribute_map = {
        'departments': 'departments',
        'teams': 'teams',
        'desk_settings': 'deskSettings',
        'skill_groups': 'skillGroups',
        'boolean_attributes': 'booleanAttributes',
        'proficiency_attributes': 'proficiencyAttributes'
    }

    def __init__(self, departments=None, teams=None, desk_settings=None, skill_groups=None, boolean_attributes=None, proficiency_attributes=None):  # noqa: E501
        """PcceAgentsFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._departments = None
        self._teams = None
        self._desk_settings = None
        self._skill_groups = None
        self._boolean_attributes = None
        self._proficiency_attributes = None
        self.discriminator = None
        if departments is not None:
            self.departments = departments
        if teams is not None:
            self.teams = teams
        if desk_settings is not None:
            self.desk_settings = desk_settings
        if skill_groups is not None:
            self.skill_groups = skill_groups
        if boolean_attributes is not None:
            self.boolean_attributes = boolean_attributes
        if proficiency_attributes is not None:
            self.proficiency_attributes = proficiency_attributes

    @property
    def departments(self):
        """Gets the departments of this PcceAgentsFieldConfigJson.  # noqa: E501


        :return: The departments of this PcceAgentsFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """Sets the departments of this PcceAgentsFieldConfigJson.


        :param departments: The departments of this PcceAgentsFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """

        self._departments = departments

    @property
    def teams(self):
        """Gets the teams of this PcceAgentsFieldConfigJson.  # noqa: E501


        :return: The teams of this PcceAgentsFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this PcceAgentsFieldConfigJson.


        :param teams: The teams of this PcceAgentsFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """

        self._teams = teams

    @property
    def desk_settings(self):
        """Gets the desk_settings of this PcceAgentsFieldConfigJson.  # noqa: E501


        :return: The desk_settings of this PcceAgentsFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._desk_settings

    @desk_settings.setter
    def desk_settings(self, desk_settings):
        """Sets the desk_settings of this PcceAgentsFieldConfigJson.


        :param desk_settings: The desk_settings of this PcceAgentsFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """

        self._desk_settings = desk_settings

    @property
    def skill_groups(self):
        """Gets the skill_groups of this PcceAgentsFieldConfigJson.  # noqa: E501


        :return: The skill_groups of this PcceAgentsFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._skill_groups

    @skill_groups.setter
    def skill_groups(self, skill_groups):
        """Sets the skill_groups of this PcceAgentsFieldConfigJson.


        :param skill_groups: The skill_groups of this PcceAgentsFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """

        self._skill_groups = skill_groups

    @property
    def boolean_attributes(self):
        """Gets the boolean_attributes of this PcceAgentsFieldConfigJson.  # noqa: E501


        :return: The boolean_attributes of this PcceAgentsFieldConfigJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._boolean_attributes

    @boolean_attributes.setter
    def boolean_attributes(self, boolean_attributes):
        """Sets the boolean_attributes of this PcceAgentsFieldConfigJson.


        :param boolean_attributes: The boolean_attributes of this PcceAgentsFieldConfigJson.  # noqa: E501
        :type: list[str]
        """

        self._boolean_attributes = boolean_attributes

    @property
    def proficiency_attributes(self):
        """Gets the proficiency_attributes of this PcceAgentsFieldConfigJson.  # noqa: E501


        :return: The proficiency_attributes of this PcceAgentsFieldConfigJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._proficiency_attributes

    @proficiency_attributes.setter
    def proficiency_attributes(self, proficiency_attributes):
        """Sets the proficiency_attributes of this PcceAgentsFieldConfigJson.


        :param proficiency_attributes: The proficiency_attributes of this PcceAgentsFieldConfigJson.  # noqa: E501
        :type: list[str]
        """

        self._proficiency_attributes = proficiency_attributes

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
        if issubclass(PcceAgentsFieldConfigJson, dict):
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
        if not isinstance(other, PcceAgentsFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
