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

class EndUserJson(object):
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
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'primary_extension': 'DirectoryNumberRefJson',
        'ipcc_extension': 'DirectoryNumberRefJson',
        'mail_id': 'str',
        'directory_uri': 'str',
        'extension_mobility_cross_cluster': 'bool',
        'uc_service_profile': 'str',
        'enable_mobility': 'bool',
        'groups': 'list[str]',
        'enable_cti': 'bool',
        'enable_mobile_voice_access': 'bool',
        'enable_home_cluster': 'bool',
        'subscribe_css': 'str',
        'self_service_user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'primary_extension': 'primaryExtension',
        'ipcc_extension': 'ipccExtension',
        'mail_id': 'mailId',
        'directory_uri': 'directoryUri',
        'extension_mobility_cross_cluster': 'extensionMobilityCrossCluster',
        'uc_service_profile': 'ucServiceProfile',
        'enable_mobility': 'enableMobility',
        'groups': 'groups',
        'enable_cti': 'enableCti',
        'enable_mobile_voice_access': 'enableMobileVoiceAccess',
        'enable_home_cluster': 'enableHomeCluster',
        'subscribe_css': 'subscribeCss',
        'self_service_user_id': 'selfServiceUserId'
    }

    def __init__(self, id=None, username=None, first_name=None, last_name=None, primary_extension=None, ipcc_extension=None, mail_id=None, directory_uri=None, extension_mobility_cross_cluster=None, uc_service_profile=None, enable_mobility=None, groups=None, enable_cti=None, enable_mobile_voice_access=None, enable_home_cluster=None, subscribe_css=None, self_service_user_id=None):  # noqa: E501
        """EndUserJson - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._primary_extension = None
        self._ipcc_extension = None
        self._mail_id = None
        self._directory_uri = None
        self._extension_mobility_cross_cluster = None
        self._uc_service_profile = None
        self._enable_mobility = None
        self._groups = None
        self._enable_cti = None
        self._enable_mobile_voice_access = None
        self._enable_home_cluster = None
        self._subscribe_css = None
        self._self_service_user_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        if primary_extension is not None:
            self.primary_extension = primary_extension
        if ipcc_extension is not None:
            self.ipcc_extension = ipcc_extension
        self.mail_id = mail_id
        self.directory_uri = directory_uri
        if extension_mobility_cross_cluster is not None:
            self.extension_mobility_cross_cluster = extension_mobility_cross_cluster
        self.uc_service_profile = uc_service_profile
        self.enable_mobility = enable_mobility
        self.groups = groups
        self.enable_cti = enable_cti
        self.enable_mobile_voice_access = enable_mobile_voice_access
        self.enable_home_cluster = enable_home_cluster
        self.subscribe_css = subscribe_css
        self.self_service_user_id = self_service_user_id

    @property
    def id(self):
        """Gets the id of this EndUserJson.  # noqa: E501


        :return: The id of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndUserJson.


        :param id: The id of this EndUserJson.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this EndUserJson.  # noqa: E501


        :return: The username of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this EndUserJson.


        :param username: The username of this EndUserJson.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this EndUserJson.  # noqa: E501


        :return: The first_name of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this EndUserJson.


        :param first_name: The first_name of this EndUserJson.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this EndUserJson.  # noqa: E501


        :return: The last_name of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this EndUserJson.


        :param last_name: The last_name of this EndUserJson.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def primary_extension(self):
        """Gets the primary_extension of this EndUserJson.  # noqa: E501


        :return: The primary_extension of this EndUserJson.  # noqa: E501
        :rtype: DirectoryNumberRefJson
        """
        return self._primary_extension

    @primary_extension.setter
    def primary_extension(self, primary_extension):
        """Sets the primary_extension of this EndUserJson.


        :param primary_extension: The primary_extension of this EndUserJson.  # noqa: E501
        :type: DirectoryNumberRefJson
        """

        self._primary_extension = primary_extension

    @property
    def ipcc_extension(self):
        """Gets the ipcc_extension of this EndUserJson.  # noqa: E501


        :return: The ipcc_extension of this EndUserJson.  # noqa: E501
        :rtype: DirectoryNumberRefJson
        """
        return self._ipcc_extension

    @ipcc_extension.setter
    def ipcc_extension(self, ipcc_extension):
        """Sets the ipcc_extension of this EndUserJson.


        :param ipcc_extension: The ipcc_extension of this EndUserJson.  # noqa: E501
        :type: DirectoryNumberRefJson
        """

        self._ipcc_extension = ipcc_extension

    @property
    def mail_id(self):
        """Gets the mail_id of this EndUserJson.  # noqa: E501


        :return: The mail_id of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._mail_id

    @mail_id.setter
    def mail_id(self, mail_id):
        """Sets the mail_id of this EndUserJson.


        :param mail_id: The mail_id of this EndUserJson.  # noqa: E501
        :type: str
        """
        if mail_id is None:
            raise ValueError("Invalid value for `mail_id`, must not be `None`")  # noqa: E501

        self._mail_id = mail_id

    @property
    def directory_uri(self):
        """Gets the directory_uri of this EndUserJson.  # noqa: E501


        :return: The directory_uri of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._directory_uri

    @directory_uri.setter
    def directory_uri(self, directory_uri):
        """Sets the directory_uri of this EndUserJson.


        :param directory_uri: The directory_uri of this EndUserJson.  # noqa: E501
        :type: str
        """
        if directory_uri is None:
            raise ValueError("Invalid value for `directory_uri`, must not be `None`")  # noqa: E501

        self._directory_uri = directory_uri

    @property
    def extension_mobility_cross_cluster(self):
        """Gets the extension_mobility_cross_cluster of this EndUserJson.  # noqa: E501


        :return: The extension_mobility_cross_cluster of this EndUserJson.  # noqa: E501
        :rtype: bool
        """
        return self._extension_mobility_cross_cluster

    @extension_mobility_cross_cluster.setter
    def extension_mobility_cross_cluster(self, extension_mobility_cross_cluster):
        """Sets the extension_mobility_cross_cluster of this EndUserJson.


        :param extension_mobility_cross_cluster: The extension_mobility_cross_cluster of this EndUserJson.  # noqa: E501
        :type: bool
        """

        self._extension_mobility_cross_cluster = extension_mobility_cross_cluster

    @property
    def uc_service_profile(self):
        """Gets the uc_service_profile of this EndUserJson.  # noqa: E501


        :return: The uc_service_profile of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._uc_service_profile

    @uc_service_profile.setter
    def uc_service_profile(self, uc_service_profile):
        """Sets the uc_service_profile of this EndUserJson.


        :param uc_service_profile: The uc_service_profile of this EndUserJson.  # noqa: E501
        :type: str
        """
        if uc_service_profile is None:
            raise ValueError("Invalid value for `uc_service_profile`, must not be `None`")  # noqa: E501

        self._uc_service_profile = uc_service_profile

    @property
    def enable_mobility(self):
        """Gets the enable_mobility of this EndUserJson.  # noqa: E501


        :return: The enable_mobility of this EndUserJson.  # noqa: E501
        :rtype: bool
        """
        return self._enable_mobility

    @enable_mobility.setter
    def enable_mobility(self, enable_mobility):
        """Sets the enable_mobility of this EndUserJson.


        :param enable_mobility: The enable_mobility of this EndUserJson.  # noqa: E501
        :type: bool
        """
        if enable_mobility is None:
            raise ValueError("Invalid value for `enable_mobility`, must not be `None`")  # noqa: E501

        self._enable_mobility = enable_mobility

    @property
    def groups(self):
        """Gets the groups of this EndUserJson.  # noqa: E501


        :return: The groups of this EndUserJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this EndUserJson.


        :param groups: The groups of this EndUserJson.  # noqa: E501
        :type: list[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def enable_cti(self):
        """Gets the enable_cti of this EndUserJson.  # noqa: E501


        :return: The enable_cti of this EndUserJson.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cti

    @enable_cti.setter
    def enable_cti(self, enable_cti):
        """Sets the enable_cti of this EndUserJson.


        :param enable_cti: The enable_cti of this EndUserJson.  # noqa: E501
        :type: bool
        """
        if enable_cti is None:
            raise ValueError("Invalid value for `enable_cti`, must not be `None`")  # noqa: E501

        self._enable_cti = enable_cti

    @property
    def enable_mobile_voice_access(self):
        """Gets the enable_mobile_voice_access of this EndUserJson.  # noqa: E501


        :return: The enable_mobile_voice_access of this EndUserJson.  # noqa: E501
        :rtype: bool
        """
        return self._enable_mobile_voice_access

    @enable_mobile_voice_access.setter
    def enable_mobile_voice_access(self, enable_mobile_voice_access):
        """Sets the enable_mobile_voice_access of this EndUserJson.


        :param enable_mobile_voice_access: The enable_mobile_voice_access of this EndUserJson.  # noqa: E501
        :type: bool
        """
        if enable_mobile_voice_access is None:
            raise ValueError("Invalid value for `enable_mobile_voice_access`, must not be `None`")  # noqa: E501

        self._enable_mobile_voice_access = enable_mobile_voice_access

    @property
    def enable_home_cluster(self):
        """Gets the enable_home_cluster of this EndUserJson.  # noqa: E501


        :return: The enable_home_cluster of this EndUserJson.  # noqa: E501
        :rtype: bool
        """
        return self._enable_home_cluster

    @enable_home_cluster.setter
    def enable_home_cluster(self, enable_home_cluster):
        """Sets the enable_home_cluster of this EndUserJson.


        :param enable_home_cluster: The enable_home_cluster of this EndUserJson.  # noqa: E501
        :type: bool
        """
        if enable_home_cluster is None:
            raise ValueError("Invalid value for `enable_home_cluster`, must not be `None`")  # noqa: E501

        self._enable_home_cluster = enable_home_cluster

    @property
    def subscribe_css(self):
        """Gets the subscribe_css of this EndUserJson.  # noqa: E501


        :return: The subscribe_css of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._subscribe_css

    @subscribe_css.setter
    def subscribe_css(self, subscribe_css):
        """Sets the subscribe_css of this EndUserJson.


        :param subscribe_css: The subscribe_css of this EndUserJson.  # noqa: E501
        :type: str
        """
        if subscribe_css is None:
            raise ValueError("Invalid value for `subscribe_css`, must not be `None`")  # noqa: E501

        self._subscribe_css = subscribe_css

    @property
    def self_service_user_id(self):
        """Gets the self_service_user_id of this EndUserJson.  # noqa: E501


        :return: The self_service_user_id of this EndUserJson.  # noqa: E501
        :rtype: str
        """
        return self._self_service_user_id

    @self_service_user_id.setter
    def self_service_user_id(self, self_service_user_id):
        """Sets the self_service_user_id of this EndUserJson.


        :param self_service_user_id: The self_service_user_id of this EndUserJson.  # noqa: E501
        :type: str
        """
        if self_service_user_id is None:
            raise ValueError("Invalid value for `self_service_user_id`, must not be `None`")  # noqa: E501

        self._self_service_user_id = self_service_user_id

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
        if issubclass(EndUserJson, dict):
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
        if not isinstance(other, EndUserJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
