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


class EndUserProvisioningSettingJson(object):
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
        'dn': 'bool',
        'agent_extension': 'bool',
        'voicemail': 'bool',
        'im_soft_phone': 'bool',
        'iphone': 'bool',
        'android': 'bool',
        'tablet': 'bool',
        'cipc': 'bool',
        'mobility': 'bool',
        'imp': 'bool',
        'snr': 'bool',
        'deskphone': 'bool',
        'site_id': 'int',
        'site_name': 'str',
        'dial_plan_groups': 'dict(str, str)'
    }

    attribute_map = {
        'dn': 'dn',
        'agent_extension': 'agentExtension',
        'voicemail': 'voicemail',
        'im_soft_phone': 'imSoftPhone',
        'iphone': 'iphone',
        'android': 'android',
        'tablet': 'tablet',
        'cipc': 'cipc',
        'mobility': 'mobility',
        'imp': 'imp',
        'snr': 'snr',
        'deskphone': 'deskphone',
        'site_id': 'siteId',
        'site_name': 'siteName',
        'dial_plan_groups': 'dialPlanGroups'
    }

    def __init__(self, dn=None, agent_extension=None, voicemail=None, im_soft_phone=None, iphone=None, android=None, tablet=None, cipc=None, mobility=None, imp=None, snr=None, deskphone=None, site_id=None, site_name=None, dial_plan_groups=None):  # noqa: E501
        """EndUserProvisioningSettingJson - a model defined in Swagger"""  # noqa: E501
        self._dn = None
        self._agent_extension = None
        self._voicemail = None
        self._im_soft_phone = None
        self._iphone = None
        self._android = None
        self._tablet = None
        self._cipc = None
        self._mobility = None
        self._imp = None
        self._snr = None
        self._deskphone = None
        self._site_id = None
        self._site_name = None
        self._dial_plan_groups = None
        self.discriminator = None
        if dn is not None:
            self.dn = dn
        if agent_extension is not None:
            self.agent_extension = agent_extension
        if voicemail is not None:
            self.voicemail = voicemail
        if im_soft_phone is not None:
            self.im_soft_phone = im_soft_phone
        if iphone is not None:
            self.iphone = iphone
        if android is not None:
            self.android = android
        if tablet is not None:
            self.tablet = tablet
        if cipc is not None:
            self.cipc = cipc
        if mobility is not None:
            self.mobility = mobility
        if imp is not None:
            self.imp = imp
        if snr is not None:
            self.snr = snr
        if deskphone is not None:
            self.deskphone = deskphone
        if site_id is not None:
            self.site_id = site_id
        if site_name is not None:
            self.site_name = site_name
        if dial_plan_groups is not None:
            self.dial_plan_groups = dial_plan_groups

    @property
    def dn(self):
        """Gets the dn of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The dn of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this EndUserProvisioningSettingJson.


        :param dn: The dn of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._dn = dn

    @property
    def agent_extension(self):
        """Gets the agent_extension of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The agent_extension of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._agent_extension

    @agent_extension.setter
    def agent_extension(self, agent_extension):
        """Sets the agent_extension of this EndUserProvisioningSettingJson.


        :param agent_extension: The agent_extension of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._agent_extension = agent_extension

    @property
    def voicemail(self):
        """Gets the voicemail of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The voicemail of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """Sets the voicemail of this EndUserProvisioningSettingJson.


        :param voicemail: The voicemail of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._voicemail = voicemail

    @property
    def im_soft_phone(self):
        """Gets the im_soft_phone of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The im_soft_phone of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._im_soft_phone

    @im_soft_phone.setter
    def im_soft_phone(self, im_soft_phone):
        """Sets the im_soft_phone of this EndUserProvisioningSettingJson.


        :param im_soft_phone: The im_soft_phone of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._im_soft_phone = im_soft_phone

    @property
    def iphone(self):
        """Gets the iphone of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The iphone of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._iphone

    @iphone.setter
    def iphone(self, iphone):
        """Sets the iphone of this EndUserProvisioningSettingJson.


        :param iphone: The iphone of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._iphone = iphone

    @property
    def android(self):
        """Gets the android of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The android of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._android

    @android.setter
    def android(self, android):
        """Sets the android of this EndUserProvisioningSettingJson.


        :param android: The android of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._android = android

    @property
    def tablet(self):
        """Gets the tablet of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The tablet of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._tablet

    @tablet.setter
    def tablet(self, tablet):
        """Sets the tablet of this EndUserProvisioningSettingJson.


        :param tablet: The tablet of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._tablet = tablet

    @property
    def cipc(self):
        """Gets the cipc of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The cipc of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._cipc

    @cipc.setter
    def cipc(self, cipc):
        """Sets the cipc of this EndUserProvisioningSettingJson.


        :param cipc: The cipc of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._cipc = cipc

    @property
    def mobility(self):
        """Gets the mobility of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The mobility of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._mobility

    @mobility.setter
    def mobility(self, mobility):
        """Sets the mobility of this EndUserProvisioningSettingJson.


        :param mobility: The mobility of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._mobility = mobility

    @property
    def imp(self):
        """Gets the imp of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The imp of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._imp

    @imp.setter
    def imp(self, imp):
        """Sets the imp of this EndUserProvisioningSettingJson.


        :param imp: The imp of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._imp = imp

    @property
    def snr(self):
        """Gets the snr of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The snr of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        """Sets the snr of this EndUserProvisioningSettingJson.


        :param snr: The snr of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._snr = snr

    @property
    def deskphone(self):
        """Gets the deskphone of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The deskphone of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: bool
        """
        return self._deskphone

    @deskphone.setter
    def deskphone(self, deskphone):
        """Sets the deskphone of this EndUserProvisioningSettingJson.


        :param deskphone: The deskphone of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: bool
        """

        self._deskphone = deskphone

    @property
    def site_id(self):
        """Gets the site_id of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The site_id of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this EndUserProvisioningSettingJson.


        :param site_id: The site_id of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def site_name(self):
        """Gets the site_name of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The site_name of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this EndUserProvisioningSettingJson.


        :param site_name: The site_name of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: str
        """

        self._site_name = site_name

    @property
    def dial_plan_groups(self):
        """Gets the dial_plan_groups of this EndUserProvisioningSettingJson.  # noqa: E501


        :return: The dial_plan_groups of this EndUserProvisioningSettingJson.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._dial_plan_groups

    @dial_plan_groups.setter
    def dial_plan_groups(self, dial_plan_groups):
        """Sets the dial_plan_groups of this EndUserProvisioningSettingJson.


        :param dial_plan_groups: The dial_plan_groups of this EndUserProvisioningSettingJson.  # noqa: E501
        :type: dict(str, str)
        """

        self._dial_plan_groups = dial_plan_groups

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
        if issubclass(EndUserProvisioningSettingJson, dict):
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
        if not isinstance(other, EndUserProvisioningSettingJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
