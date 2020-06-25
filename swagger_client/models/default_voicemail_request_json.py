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


class DefaultVoicemailRequestJson(object):
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
        'site_id': 'str',
        'end_user_username': 'str'
    }

    attribute_map = {
        'site_id': 'siteId',
        'end_user_username': 'endUserUsername'
    }

    def __init__(self, site_id=None, end_user_username=None):  # noqa: E501
        """DefaultVoicemailRequestJson - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._end_user_username = None
        self.discriminator = None
        self.site_id = site_id
        self.end_user_username = end_user_username

    @property
    def site_id(self):
        """Gets the site_id of this DefaultVoicemailRequestJson.  # noqa: E501


        :return: The site_id of this DefaultVoicemailRequestJson.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this DefaultVoicemailRequestJson.


        :param site_id: The site_id of this DefaultVoicemailRequestJson.  # noqa: E501
        :type: str
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def end_user_username(self):
        """Gets the end_user_username of this DefaultVoicemailRequestJson.  # noqa: E501


        :return: The end_user_username of this DefaultVoicemailRequestJson.  # noqa: E501
        :rtype: str
        """
        return self._end_user_username

    @end_user_username.setter
    def end_user_username(self, end_user_username):
        """Sets the end_user_username of this DefaultVoicemailRequestJson.


        :param end_user_username: The end_user_username of this DefaultVoicemailRequestJson.  # noqa: E501
        :type: str
        """
        if end_user_username is None:
            raise ValueError("Invalid value for `end_user_username`, must not be `None`")  # noqa: E501

        self._end_user_username = end_user_username

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
        if issubclass(DefaultVoicemailRequestJson, dict):
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
        if not isinstance(other, DefaultVoicemailRequestJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
