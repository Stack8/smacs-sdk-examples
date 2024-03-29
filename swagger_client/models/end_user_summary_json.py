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

class EndUserSummaryJson(object):
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
        'user': 'EndUserResultJson',
        'ldap_user': 'LdapUserJson',
        'uccx_agents': 'list[UccxAgentRefJson]',
        'mail_id': 'str',
        'im_presence_active': 'bool',
        'primary_extension': 'DnDetailSummaryJson',
        'ipcc_extension': 'DnDetailSummaryJson',
        'phones': 'list[PhoneSummaryJson]',
        'snr': 'SnrSummaryJson',
        'extension_mobilities': 'list[ExtensionMobilitySummaryJson]',
        'associated_public_phones': 'list[PhoneSummaryJson]',
        'additional_extensions': 'list[DirectoryNumberResultJson]',
        'sites': 'list[SiteSearchResultJson]',
        'type': 'str'
    }

    attribute_map = {
        'user': 'user',
        'ldap_user': 'ldapUser',
        'uccx_agents': 'uccxAgents',
        'mail_id': 'mailId',
        'im_presence_active': 'imPresenceActive',
        'primary_extension': 'primaryExtension',
        'ipcc_extension': 'ipccExtension',
        'phones': 'phones',
        'snr': 'snr',
        'extension_mobilities': 'extensionMobilities',
        'associated_public_phones': 'associatedPublicPhones',
        'additional_extensions': 'additionalExtensions',
        'sites': 'sites',
        'type': 'type'
    }

    def __init__(self, user=None, ldap_user=None, uccx_agents=None, mail_id=None, im_presence_active=None, primary_extension=None, ipcc_extension=None, phones=None, snr=None, extension_mobilities=None, associated_public_phones=None, additional_extensions=None, sites=None, type=None):  # noqa: E501
        """EndUserSummaryJson - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._ldap_user = None
        self._uccx_agents = None
        self._mail_id = None
        self._im_presence_active = None
        self._primary_extension = None
        self._ipcc_extension = None
        self._phones = None
        self._snr = None
        self._extension_mobilities = None
        self._associated_public_phones = None
        self._additional_extensions = None
        self._sites = None
        self._type = None
        self.discriminator = None
        if user is not None:
            self.user = user
        if ldap_user is not None:
            self.ldap_user = ldap_user
        if uccx_agents is not None:
            self.uccx_agents = uccx_agents
        if mail_id is not None:
            self.mail_id = mail_id
        if im_presence_active is not None:
            self.im_presence_active = im_presence_active
        if primary_extension is not None:
            self.primary_extension = primary_extension
        if ipcc_extension is not None:
            self.ipcc_extension = ipcc_extension
        if phones is not None:
            self.phones = phones
        if snr is not None:
            self.snr = snr
        if extension_mobilities is not None:
            self.extension_mobilities = extension_mobilities
        if associated_public_phones is not None:
            self.associated_public_phones = associated_public_phones
        if additional_extensions is not None:
            self.additional_extensions = additional_extensions
        if sites is not None:
            self.sites = sites
        if type is not None:
            self.type = type

    @property
    def user(self):
        """Gets the user of this EndUserSummaryJson.  # noqa: E501


        :return: The user of this EndUserSummaryJson.  # noqa: E501
        :rtype: EndUserResultJson
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this EndUserSummaryJson.


        :param user: The user of this EndUserSummaryJson.  # noqa: E501
        :type: EndUserResultJson
        """

        self._user = user

    @property
    def ldap_user(self):
        """Gets the ldap_user of this EndUserSummaryJson.  # noqa: E501


        :return: The ldap_user of this EndUserSummaryJson.  # noqa: E501
        :rtype: LdapUserJson
        """
        return self._ldap_user

    @ldap_user.setter
    def ldap_user(self, ldap_user):
        """Sets the ldap_user of this EndUserSummaryJson.


        :param ldap_user: The ldap_user of this EndUserSummaryJson.  # noqa: E501
        :type: LdapUserJson
        """

        self._ldap_user = ldap_user

    @property
    def uccx_agents(self):
        """Gets the uccx_agents of this EndUserSummaryJson.  # noqa: E501


        :return: The uccx_agents of this EndUserSummaryJson.  # noqa: E501
        :rtype: list[UccxAgentRefJson]
        """
        return self._uccx_agents

    @uccx_agents.setter
    def uccx_agents(self, uccx_agents):
        """Sets the uccx_agents of this EndUserSummaryJson.


        :param uccx_agents: The uccx_agents of this EndUserSummaryJson.  # noqa: E501
        :type: list[UccxAgentRefJson]
        """

        self._uccx_agents = uccx_agents

    @property
    def mail_id(self):
        """Gets the mail_id of this EndUserSummaryJson.  # noqa: E501


        :return: The mail_id of this EndUserSummaryJson.  # noqa: E501
        :rtype: str
        """
        return self._mail_id

    @mail_id.setter
    def mail_id(self, mail_id):
        """Sets the mail_id of this EndUserSummaryJson.


        :param mail_id: The mail_id of this EndUserSummaryJson.  # noqa: E501
        :type: str
        """

        self._mail_id = mail_id

    @property
    def im_presence_active(self):
        """Gets the im_presence_active of this EndUserSummaryJson.  # noqa: E501


        :return: The im_presence_active of this EndUserSummaryJson.  # noqa: E501
        :rtype: bool
        """
        return self._im_presence_active

    @im_presence_active.setter
    def im_presence_active(self, im_presence_active):
        """Sets the im_presence_active of this EndUserSummaryJson.


        :param im_presence_active: The im_presence_active of this EndUserSummaryJson.  # noqa: E501
        :type: bool
        """

        self._im_presence_active = im_presence_active

    @property
    def primary_extension(self):
        """Gets the primary_extension of this EndUserSummaryJson.  # noqa: E501


        :return: The primary_extension of this EndUserSummaryJson.  # noqa: E501
        :rtype: DnDetailSummaryJson
        """
        return self._primary_extension

    @primary_extension.setter
    def primary_extension(self, primary_extension):
        """Sets the primary_extension of this EndUserSummaryJson.


        :param primary_extension: The primary_extension of this EndUserSummaryJson.  # noqa: E501
        :type: DnDetailSummaryJson
        """

        self._primary_extension = primary_extension

    @property
    def ipcc_extension(self):
        """Gets the ipcc_extension of this EndUserSummaryJson.  # noqa: E501


        :return: The ipcc_extension of this EndUserSummaryJson.  # noqa: E501
        :rtype: DnDetailSummaryJson
        """
        return self._ipcc_extension

    @ipcc_extension.setter
    def ipcc_extension(self, ipcc_extension):
        """Sets the ipcc_extension of this EndUserSummaryJson.


        :param ipcc_extension: The ipcc_extension of this EndUserSummaryJson.  # noqa: E501
        :type: DnDetailSummaryJson
        """

        self._ipcc_extension = ipcc_extension

    @property
    def phones(self):
        """Gets the phones of this EndUserSummaryJson.  # noqa: E501


        :return: The phones of this EndUserSummaryJson.  # noqa: E501
        :rtype: list[PhoneSummaryJson]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this EndUserSummaryJson.


        :param phones: The phones of this EndUserSummaryJson.  # noqa: E501
        :type: list[PhoneSummaryJson]
        """

        self._phones = phones

    @property
    def snr(self):
        """Gets the snr of this EndUserSummaryJson.  # noqa: E501


        :return: The snr of this EndUserSummaryJson.  # noqa: E501
        :rtype: SnrSummaryJson
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        """Sets the snr of this EndUserSummaryJson.


        :param snr: The snr of this EndUserSummaryJson.  # noqa: E501
        :type: SnrSummaryJson
        """

        self._snr = snr

    @property
    def extension_mobilities(self):
        """Gets the extension_mobilities of this EndUserSummaryJson.  # noqa: E501


        :return: The extension_mobilities of this EndUserSummaryJson.  # noqa: E501
        :rtype: list[ExtensionMobilitySummaryJson]
        """
        return self._extension_mobilities

    @extension_mobilities.setter
    def extension_mobilities(self, extension_mobilities):
        """Sets the extension_mobilities of this EndUserSummaryJson.


        :param extension_mobilities: The extension_mobilities of this EndUserSummaryJson.  # noqa: E501
        :type: list[ExtensionMobilitySummaryJson]
        """

        self._extension_mobilities = extension_mobilities

    @property
    def associated_public_phones(self):
        """Gets the associated_public_phones of this EndUserSummaryJson.  # noqa: E501


        :return: The associated_public_phones of this EndUserSummaryJson.  # noqa: E501
        :rtype: list[PhoneSummaryJson]
        """
        return self._associated_public_phones

    @associated_public_phones.setter
    def associated_public_phones(self, associated_public_phones):
        """Sets the associated_public_phones of this EndUserSummaryJson.


        :param associated_public_phones: The associated_public_phones of this EndUserSummaryJson.  # noqa: E501
        :type: list[PhoneSummaryJson]
        """

        self._associated_public_phones = associated_public_phones

    @property
    def additional_extensions(self):
        """Gets the additional_extensions of this EndUserSummaryJson.  # noqa: E501


        :return: The additional_extensions of this EndUserSummaryJson.  # noqa: E501
        :rtype: list[DirectoryNumberResultJson]
        """
        return self._additional_extensions

    @additional_extensions.setter
    def additional_extensions(self, additional_extensions):
        """Sets the additional_extensions of this EndUserSummaryJson.


        :param additional_extensions: The additional_extensions of this EndUserSummaryJson.  # noqa: E501
        :type: list[DirectoryNumberResultJson]
        """

        self._additional_extensions = additional_extensions

    @property
    def sites(self):
        """Gets the sites of this EndUserSummaryJson.  # noqa: E501


        :return: The sites of this EndUserSummaryJson.  # noqa: E501
        :rtype: list[SiteSearchResultJson]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this EndUserSummaryJson.


        :param sites: The sites of this EndUserSummaryJson.  # noqa: E501
        :type: list[SiteSearchResultJson]
        """

        self._sites = sites

    @property
    def type(self):
        """Gets the type of this EndUserSummaryJson.  # noqa: E501


        :return: The type of this EndUserSummaryJson.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EndUserSummaryJson.


        :param type: The type of this EndUserSummaryJson.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(EndUserSummaryJson, dict):
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
        if not isinstance(other, EndUserSummaryJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
