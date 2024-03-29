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

class UccxAgentJson(object):
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
        'id': 'str',
        'type': 'int',
        'resource_group': 'str',
        'automatic_available': 'bool',
        'team': 'str',
        'alias': 'str',
        'skills': 'list[UccxAgentSkillJson]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'resource_group': 'resourceGroup',
        'automatic_available': 'automaticAvailable',
        'team': 'team',
        'alias': 'alias',
        'skills': 'skills'
    }

    def __init__(self, id=None, type=None, resource_group=None, automatic_available=None, team=None, alias=None, skills=None):  # noqa: E501
        """UccxAgentJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._resource_group = None
        self._automatic_available = None
        self._team = None
        self._alias = None
        self._skills = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.type = type
        self.resource_group = resource_group
        self.automatic_available = automatic_available
        self.team = team
        self.alias = alias
        self.skills = skills

    @property
    def id(self):
        """Gets the id of this UccxAgentJson.  # noqa: E501


        :return: The id of this UccxAgentJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UccxAgentJson.


        :param id: The id of this UccxAgentJson.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this UccxAgentJson.  # noqa: E501


        :return: The type of this UccxAgentJson.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UccxAgentJson.


        :param type: The type of this UccxAgentJson.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def resource_group(self):
        """Gets the resource_group of this UccxAgentJson.  # noqa: E501


        :return: The resource_group of this UccxAgentJson.  # noqa: E501
        :rtype: str
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this UccxAgentJson.


        :param resource_group: The resource_group of this UccxAgentJson.  # noqa: E501
        :type: str
        """
        if resource_group is None:
            raise ValueError("Invalid value for `resource_group`, must not be `None`")  # noqa: E501

        self._resource_group = resource_group

    @property
    def automatic_available(self):
        """Gets the automatic_available of this UccxAgentJson.  # noqa: E501


        :return: The automatic_available of this UccxAgentJson.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_available

    @automatic_available.setter
    def automatic_available(self, automatic_available):
        """Sets the automatic_available of this UccxAgentJson.


        :param automatic_available: The automatic_available of this UccxAgentJson.  # noqa: E501
        :type: bool
        """
        if automatic_available is None:
            raise ValueError("Invalid value for `automatic_available`, must not be `None`")  # noqa: E501

        self._automatic_available = automatic_available

    @property
    def team(self):
        """Gets the team of this UccxAgentJson.  # noqa: E501


        :return: The team of this UccxAgentJson.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this UccxAgentJson.


        :param team: The team of this UccxAgentJson.  # noqa: E501
        :type: str
        """
        if team is None:
            raise ValueError("Invalid value for `team`, must not be `None`")  # noqa: E501

        self._team = team

    @property
    def alias(self):
        """Gets the alias of this UccxAgentJson.  # noqa: E501


        :return: The alias of this UccxAgentJson.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this UccxAgentJson.


        :param alias: The alias of this UccxAgentJson.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def skills(self):
        """Gets the skills of this UccxAgentJson.  # noqa: E501


        :return: The skills of this UccxAgentJson.  # noqa: E501
        :rtype: list[UccxAgentSkillJson]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this UccxAgentJson.


        :param skills: The skills of this UccxAgentJson.  # noqa: E501
        :type: list[UccxAgentSkillJson]
        """
        if skills is None:
            raise ValueError("Invalid value for `skills`, must not be `None`")  # noqa: E501

        self._skills = skills

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
        if issubclass(UccxAgentJson, dict):
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
        if not isinstance(other, UccxAgentJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
