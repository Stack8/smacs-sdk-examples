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


class DistributionListMemberJson(object):
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
        'voicemail_id': 'str',
        'alias': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'voicemail_id': 'voicemailId',
        'alias': 'alias',
        'display_name': 'displayName'
    }

    def __init__(self, id=None, voicemail_id=None, alias=None, display_name=None):  # noqa: E501
        """DistributionListMemberJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._voicemail_id = None
        self._alias = None
        self._display_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if voicemail_id is not None:
            self.voicemail_id = voicemail_id
        self.alias = alias
        self.display_name = display_name

    @property
    def id(self):
        """Gets the id of this DistributionListMemberJson.  # noqa: E501


        :return: The id of this DistributionListMemberJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DistributionListMemberJson.


        :param id: The id of this DistributionListMemberJson.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def voicemail_id(self):
        """Gets the voicemail_id of this DistributionListMemberJson.  # noqa: E501


        :return: The voicemail_id of this DistributionListMemberJson.  # noqa: E501
        :rtype: str
        """
        return self._voicemail_id

    @voicemail_id.setter
    def voicemail_id(self, voicemail_id):
        """Sets the voicemail_id of this DistributionListMemberJson.


        :param voicemail_id: The voicemail_id of this DistributionListMemberJson.  # noqa: E501
        :type: str
        """

        self._voicemail_id = voicemail_id

    @property
    def alias(self):
        """Gets the alias of this DistributionListMemberJson.  # noqa: E501


        :return: The alias of this DistributionListMemberJson.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this DistributionListMemberJson.


        :param alias: The alias of this DistributionListMemberJson.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def display_name(self):
        """Gets the display_name of this DistributionListMemberJson.  # noqa: E501


        :return: The display_name of this DistributionListMemberJson.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DistributionListMemberJson.


        :param display_name: The display_name of this DistributionListMemberJson.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

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
        if issubclass(DistributionListMemberJson, dict):
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
        if not isinstance(other, DistributionListMemberJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
