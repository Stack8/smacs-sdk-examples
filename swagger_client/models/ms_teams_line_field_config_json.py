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

class MsTeamsLineFieldConfigJson(object):
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
        'tenant_dial_plan': 'SelectFieldConfigJson',
        'online_voice_routing_policy': 'SelectFieldConfigJson',
        'emergency_calling_policy': 'SelectFieldConfigJson',
        'emergency_call_routing_policy': 'SelectFieldConfigJson',
        'hosted_voice_mail': 'CustomCheckboxFieldConfigJson',
        'on_prem_line_uri_extension': 'TextFieldConfigJson'
    }

    attribute_map = {
        'tenant_dial_plan': 'tenantDialPlan',
        'online_voice_routing_policy': 'onlineVoiceRoutingPolicy',
        'emergency_calling_policy': 'emergencyCallingPolicy',
        'emergency_call_routing_policy': 'emergencyCallRoutingPolicy',
        'hosted_voice_mail': 'hostedVoiceMail',
        'on_prem_line_uri_extension': 'onPremLineUriExtension'
    }

    def __init__(self, tenant_dial_plan=None, online_voice_routing_policy=None, emergency_calling_policy=None, emergency_call_routing_policy=None, hosted_voice_mail=None, on_prem_line_uri_extension=None):  # noqa: E501
        """MsTeamsLineFieldConfigJson - a model defined in Swagger"""  # noqa: E501
        self._tenant_dial_plan = None
        self._online_voice_routing_policy = None
        self._emergency_calling_policy = None
        self._emergency_call_routing_policy = None
        self._hosted_voice_mail = None
        self._on_prem_line_uri_extension = None
        self.discriminator = None
        self.tenant_dial_plan = tenant_dial_plan
        self.online_voice_routing_policy = online_voice_routing_policy
        self.emergency_calling_policy = emergency_calling_policy
        self.emergency_call_routing_policy = emergency_call_routing_policy
        self.hosted_voice_mail = hosted_voice_mail
        self.on_prem_line_uri_extension = on_prem_line_uri_extension

    @property
    def tenant_dial_plan(self):
        """Gets the tenant_dial_plan of this MsTeamsLineFieldConfigJson.  # noqa: E501


        :return: The tenant_dial_plan of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._tenant_dial_plan

    @tenant_dial_plan.setter
    def tenant_dial_plan(self, tenant_dial_plan):
        """Sets the tenant_dial_plan of this MsTeamsLineFieldConfigJson.


        :param tenant_dial_plan: The tenant_dial_plan of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if tenant_dial_plan is None:
            raise ValueError("Invalid value for `tenant_dial_plan`, must not be `None`")  # noqa: E501

        self._tenant_dial_plan = tenant_dial_plan

    @property
    def online_voice_routing_policy(self):
        """Gets the online_voice_routing_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501


        :return: The online_voice_routing_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._online_voice_routing_policy

    @online_voice_routing_policy.setter
    def online_voice_routing_policy(self, online_voice_routing_policy):
        """Sets the online_voice_routing_policy of this MsTeamsLineFieldConfigJson.


        :param online_voice_routing_policy: The online_voice_routing_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if online_voice_routing_policy is None:
            raise ValueError("Invalid value for `online_voice_routing_policy`, must not be `None`")  # noqa: E501

        self._online_voice_routing_policy = online_voice_routing_policy

    @property
    def emergency_calling_policy(self):
        """Gets the emergency_calling_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501


        :return: The emergency_calling_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._emergency_calling_policy

    @emergency_calling_policy.setter
    def emergency_calling_policy(self, emergency_calling_policy):
        """Sets the emergency_calling_policy of this MsTeamsLineFieldConfigJson.


        :param emergency_calling_policy: The emergency_calling_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if emergency_calling_policy is None:
            raise ValueError("Invalid value for `emergency_calling_policy`, must not be `None`")  # noqa: E501

        self._emergency_calling_policy = emergency_calling_policy

    @property
    def emergency_call_routing_policy(self):
        """Gets the emergency_call_routing_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501


        :return: The emergency_call_routing_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :rtype: SelectFieldConfigJson
        """
        return self._emergency_call_routing_policy

    @emergency_call_routing_policy.setter
    def emergency_call_routing_policy(self, emergency_call_routing_policy):
        """Sets the emergency_call_routing_policy of this MsTeamsLineFieldConfigJson.


        :param emergency_call_routing_policy: The emergency_call_routing_policy of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :type: SelectFieldConfigJson
        """
        if emergency_call_routing_policy is None:
            raise ValueError("Invalid value for `emergency_call_routing_policy`, must not be `None`")  # noqa: E501

        self._emergency_call_routing_policy = emergency_call_routing_policy

    @property
    def hosted_voice_mail(self):
        """Gets the hosted_voice_mail of this MsTeamsLineFieldConfigJson.  # noqa: E501


        :return: The hosted_voice_mail of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :rtype: CustomCheckboxFieldConfigJson
        """
        return self._hosted_voice_mail

    @hosted_voice_mail.setter
    def hosted_voice_mail(self, hosted_voice_mail):
        """Sets the hosted_voice_mail of this MsTeamsLineFieldConfigJson.


        :param hosted_voice_mail: The hosted_voice_mail of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :type: CustomCheckboxFieldConfigJson
        """
        if hosted_voice_mail is None:
            raise ValueError("Invalid value for `hosted_voice_mail`, must not be `None`")  # noqa: E501

        self._hosted_voice_mail = hosted_voice_mail

    @property
    def on_prem_line_uri_extension(self):
        """Gets the on_prem_line_uri_extension of this MsTeamsLineFieldConfigJson.  # noqa: E501


        :return: The on_prem_line_uri_extension of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :rtype: TextFieldConfigJson
        """
        return self._on_prem_line_uri_extension

    @on_prem_line_uri_extension.setter
    def on_prem_line_uri_extension(self, on_prem_line_uri_extension):
        """Sets the on_prem_line_uri_extension of this MsTeamsLineFieldConfigJson.


        :param on_prem_line_uri_extension: The on_prem_line_uri_extension of this MsTeamsLineFieldConfigJson.  # noqa: E501
        :type: TextFieldConfigJson
        """
        if on_prem_line_uri_extension is None:
            raise ValueError("Invalid value for `on_prem_line_uri_extension`, must not be `None`")  # noqa: E501

        self._on_prem_line_uri_extension = on_prem_line_uri_extension

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
        if issubclass(MsTeamsLineFieldConfigJson, dict):
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
        if not isinstance(other, MsTeamsLineFieldConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other