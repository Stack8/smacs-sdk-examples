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

class BuildPropertiesJson(object):
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
        'build_version': 'str',
        'build_timestamp': 'str',
        'git_describe': 'str',
        'show_instruction_guide': 'bool'
    }

    attribute_map = {
        'build_version': 'buildVersion',
        'build_timestamp': 'buildTimestamp',
        'git_describe': 'gitDescribe',
        'show_instruction_guide': 'showInstructionGuide'
    }

    def __init__(self, build_version=None, build_timestamp=None, git_describe=None, show_instruction_guide=None):  # noqa: E501
        """BuildPropertiesJson - a model defined in Swagger"""  # noqa: E501
        self._build_version = None
        self._build_timestamp = None
        self._git_describe = None
        self._show_instruction_guide = None
        self.discriminator = None
        self.build_version = build_version
        self.build_timestamp = build_timestamp
        self.git_describe = git_describe
        if show_instruction_guide is not None:
            self.show_instruction_guide = show_instruction_guide

    @property
    def build_version(self):
        """Gets the build_version of this BuildPropertiesJson.  # noqa: E501


        :return: The build_version of this BuildPropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this BuildPropertiesJson.


        :param build_version: The build_version of this BuildPropertiesJson.  # noqa: E501
        :type: str
        """
        if build_version is None:
            raise ValueError("Invalid value for `build_version`, must not be `None`")  # noqa: E501

        self._build_version = build_version

    @property
    def build_timestamp(self):
        """Gets the build_timestamp of this BuildPropertiesJson.  # noqa: E501


        :return: The build_timestamp of this BuildPropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._build_timestamp

    @build_timestamp.setter
    def build_timestamp(self, build_timestamp):
        """Sets the build_timestamp of this BuildPropertiesJson.


        :param build_timestamp: The build_timestamp of this BuildPropertiesJson.  # noqa: E501
        :type: str
        """
        if build_timestamp is None:
            raise ValueError("Invalid value for `build_timestamp`, must not be `None`")  # noqa: E501

        self._build_timestamp = build_timestamp

    @property
    def git_describe(self):
        """Gets the git_describe of this BuildPropertiesJson.  # noqa: E501


        :return: The git_describe of this BuildPropertiesJson.  # noqa: E501
        :rtype: str
        """
        return self._git_describe

    @git_describe.setter
    def git_describe(self, git_describe):
        """Sets the git_describe of this BuildPropertiesJson.


        :param git_describe: The git_describe of this BuildPropertiesJson.  # noqa: E501
        :type: str
        """
        if git_describe is None:
            raise ValueError("Invalid value for `git_describe`, must not be `None`")  # noqa: E501

        self._git_describe = git_describe

    @property
    def show_instruction_guide(self):
        """Gets the show_instruction_guide of this BuildPropertiesJson.  # noqa: E501


        :return: The show_instruction_guide of this BuildPropertiesJson.  # noqa: E501
        :rtype: bool
        """
        return self._show_instruction_guide

    @show_instruction_guide.setter
    def show_instruction_guide(self, show_instruction_guide):
        """Sets the show_instruction_guide of this BuildPropertiesJson.


        :param show_instruction_guide: The show_instruction_guide of this BuildPropertiesJson.  # noqa: E501
        :type: bool
        """

        self._show_instruction_guide = show_instruction_guide

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
        if issubclass(BuildPropertiesJson, dict):
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
        if not isinstance(other, BuildPropertiesJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
