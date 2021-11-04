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

class MicrosoftDialPlanEntryJson(object):
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
        'e164_line_uri': 'str',
        'status': 'str',
        'associated_user': 'Microsoft365UserRefJson',
        'deletion_date': 'str'
    }

    attribute_map = {
        'e164_line_uri': 'e164LineUri',
        'status': 'status',
        'associated_user': 'associatedUser',
        'deletion_date': 'deletionDate'
    }

    def __init__(self, e164_line_uri=None, status=None, associated_user=None, deletion_date=None):  # noqa: E501
        """MicrosoftDialPlanEntryJson - a model defined in Swagger"""  # noqa: E501
        self._e164_line_uri = None
        self._status = None
        self._associated_user = None
        self._deletion_date = None
        self.discriminator = None
        self.e164_line_uri = e164_line_uri
        self.status = status
        if associated_user is not None:
            self.associated_user = associated_user
        if deletion_date is not None:
            self.deletion_date = deletion_date

    @property
    def e164_line_uri(self):
        """Gets the e164_line_uri of this MicrosoftDialPlanEntryJson.  # noqa: E501


        :return: The e164_line_uri of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :rtype: str
        """
        return self._e164_line_uri

    @e164_line_uri.setter
    def e164_line_uri(self, e164_line_uri):
        """Sets the e164_line_uri of this MicrosoftDialPlanEntryJson.


        :param e164_line_uri: The e164_line_uri of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :type: str
        """
        if e164_line_uri is None:
            raise ValueError("Invalid value for `e164_line_uri`, must not be `None`")  # noqa: E501

        self._e164_line_uri = e164_line_uri

    @property
    def status(self):
        """Gets the status of this MicrosoftDialPlanEntryJson.  # noqa: E501


        :return: The status of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MicrosoftDialPlanEntryJson.


        :param status: The status of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ASSIGNED", "UNASSIGNED", "RECENTLY_UNASSIGNED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def associated_user(self):
        """Gets the associated_user of this MicrosoftDialPlanEntryJson.  # noqa: E501


        :return: The associated_user of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :rtype: Microsoft365UserRefJson
        """
        return self._associated_user

    @associated_user.setter
    def associated_user(self, associated_user):
        """Sets the associated_user of this MicrosoftDialPlanEntryJson.


        :param associated_user: The associated_user of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :type: Microsoft365UserRefJson
        """

        self._associated_user = associated_user

    @property
    def deletion_date(self):
        """Gets the deletion_date of this MicrosoftDialPlanEntryJson.  # noqa: E501


        :return: The deletion_date of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :rtype: str
        """
        return self._deletion_date

    @deletion_date.setter
    def deletion_date(self, deletion_date):
        """Sets the deletion_date of this MicrosoftDialPlanEntryJson.


        :param deletion_date: The deletion_date of this MicrosoftDialPlanEntryJson.  # noqa: E501
        :type: str
        """

        self._deletion_date = deletion_date

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
        if issubclass(MicrosoftDialPlanEntryJson, dict):
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
        if not isinstance(other, MicrosoftDialPlanEntryJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other