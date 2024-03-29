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

class PostVoicemailJson(object):
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
        'alias': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'display_name': 'str',
        'extension': 'str',
        'template': 'str'
    }

    attribute_map = {
        'id': 'id',
        'alias': 'alias',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'display_name': 'displayName',
        'extension': 'extension',
        'template': 'template'
    }

    def __init__(self, id=None, alias=None, first_name=None, last_name=None, display_name=None, extension=None, template=None):  # noqa: E501
        """PostVoicemailJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._alias = None
        self._first_name = None
        self._last_name = None
        self._display_name = None
        self._extension = None
        self._template = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.alias = alias
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.extension = extension
        self.template = template

    @property
    def id(self):
        """Gets the id of this PostVoicemailJson.  # noqa: E501


        :return: The id of this PostVoicemailJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostVoicemailJson.


        :param id: The id of this PostVoicemailJson.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def alias(self):
        """Gets the alias of this PostVoicemailJson.  # noqa: E501


        :return: The alias of this PostVoicemailJson.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PostVoicemailJson.


        :param alias: The alias of this PostVoicemailJson.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def first_name(self):
        """Gets the first_name of this PostVoicemailJson.  # noqa: E501


        :return: The first_name of this PostVoicemailJson.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PostVoicemailJson.


        :param first_name: The first_name of this PostVoicemailJson.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PostVoicemailJson.  # noqa: E501


        :return: The last_name of this PostVoicemailJson.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PostVoicemailJson.


        :param last_name: The last_name of this PostVoicemailJson.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def display_name(self):
        """Gets the display_name of this PostVoicemailJson.  # noqa: E501


        :return: The display_name of this PostVoicemailJson.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PostVoicemailJson.


        :param display_name: The display_name of this PostVoicemailJson.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def extension(self):
        """Gets the extension of this PostVoicemailJson.  # noqa: E501


        :return: The extension of this PostVoicemailJson.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this PostVoicemailJson.


        :param extension: The extension of this PostVoicemailJson.  # noqa: E501
        :type: str
        """
        if extension is None:
            raise ValueError("Invalid value for `extension`, must not be `None`")  # noqa: E501

        self._extension = extension

    @property
    def template(self):
        """Gets the template of this PostVoicemailJson.  # noqa: E501


        :return: The template of this PostVoicemailJson.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this PostVoicemailJson.


        :param template: The template of this PostVoicemailJson.  # noqa: E501
        :type: str
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

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
        if issubclass(PostVoicemailJson, dict):
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
        if not isinstance(other, PostVoicemailJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
