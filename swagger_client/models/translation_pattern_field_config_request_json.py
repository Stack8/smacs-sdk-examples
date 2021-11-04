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

class TranslationPatternFieldConfigRequestJson(object):
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
        'extension': 'str',
        'username': 'str',
        'dial_plan_group_id': 'int',
        'site_id': 'int'
    }

    attribute_map = {
        'extension': 'extension',
        'username': 'username',
        'dial_plan_group_id': 'dialPlanGroupId',
        'site_id': 'siteId'
    }

    def __init__(self, extension=None, username=None, dial_plan_group_id=None, site_id=None):  # noqa: E501
        """TranslationPatternFieldConfigRequestJson - a model defined in Swagger"""  # noqa: E501
        self._extension = None
        self._username = None
        self._dial_plan_group_id = None
        self._site_id = None
        self.discriminator = None
        self.extension = extension
        if username is not None:
            self.username = username
        self.dial_plan_group_id = dial_plan_group_id
        self.site_id = site_id

    @property
    def extension(self):
        """Gets the extension of this TranslationPatternFieldConfigRequestJson.  # noqa: E501


        :return: The extension of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this TranslationPatternFieldConfigRequestJson.


        :param extension: The extension of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :type: str
        """
        if extension is None:
            raise ValueError("Invalid value for `extension`, must not be `None`")  # noqa: E501

        self._extension = extension

    @property
    def username(self):
        """Gets the username of this TranslationPatternFieldConfigRequestJson.  # noqa: E501


        :return: The username of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TranslationPatternFieldConfigRequestJson.


        :param username: The username of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def dial_plan_group_id(self):
        """Gets the dial_plan_group_id of this TranslationPatternFieldConfigRequestJson.  # noqa: E501


        :return: The dial_plan_group_id of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :rtype: int
        """
        return self._dial_plan_group_id

    @dial_plan_group_id.setter
    def dial_plan_group_id(self, dial_plan_group_id):
        """Sets the dial_plan_group_id of this TranslationPatternFieldConfigRequestJson.


        :param dial_plan_group_id: The dial_plan_group_id of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :type: int
        """
        if dial_plan_group_id is None:
            raise ValueError("Invalid value for `dial_plan_group_id`, must not be `None`")  # noqa: E501

        self._dial_plan_group_id = dial_plan_group_id

    @property
    def site_id(self):
        """Gets the site_id of this TranslationPatternFieldConfigRequestJson.  # noqa: E501


        :return: The site_id of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this TranslationPatternFieldConfigRequestJson.


        :param site_id: The site_id of this TranslationPatternFieldConfigRequestJson.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

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
        if issubclass(TranslationPatternFieldConfigRequestJson, dict):
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
        if not isinstance(other, TranslationPatternFieldConfigRequestJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
