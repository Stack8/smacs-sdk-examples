# coding: utf-8

"""
    SMACS REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 7.2.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EndUserProvisioningApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_cisco_end_user_provisioning_settings(self, **kwargs):  # noqa: E501
        """Get the provisioning settings available across all sites  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_cisco_end_user_provisioning_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EndUserProvisioningSettingJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_cisco_end_user_provisioning_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_cisco_end_user_provisioning_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_cisco_end_user_provisioning_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Get the provisioning settings available across all sites  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_cisco_end_user_provisioning_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EndUserProvisioningSettingJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_cisco_end_user_provisioning_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zero-touch/cisco/end-user-provisioning-settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EndUserProvisioningSettingJson]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_end_user_provisioning_settings(self, **kwargs):  # noqa: E501
        """Get the provisioning settings available across all sites  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_end_user_provisioning_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EndUserProvisioningSettingJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_end_user_provisioning_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_end_user_provisioning_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_end_user_provisioning_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Get the provisioning settings available across all sites  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_end_user_provisioning_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EndUserProvisioningSettingJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_end_user_provisioning_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zero-touch/end-user-provisioning-settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EndUserProvisioningSettingJson]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cisco_end_user_provisioning_setting(self, site_id, **kwargs):  # noqa: E501
        """Get the provisioning settings available on the given site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cisco_end_user_provisioning_setting(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The id of the site (required)
        :return: EndUserProvisioningSettingJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cisco_end_user_provisioning_setting_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cisco_end_user_provisioning_setting_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def get_cisco_end_user_provisioning_setting_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """Get the provisioning settings available on the given site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cisco_end_user_provisioning_setting_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The id of the site (required)
        :return: EndUserProvisioningSettingJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cisco_end_user_provisioning_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_cisco_end_user_provisioning_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zero-touch/cisco/end-user-provisioning-settings/{siteId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EndUserProvisioningSettingJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_end_user_provisioning_setting(self, site_id, **kwargs):  # noqa: E501
        """Get the provisioning settings available on the given site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_end_user_provisioning_setting(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The id of the site (required)
        :return: EndUserProvisioningSettingJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_end_user_provisioning_setting_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_end_user_provisioning_setting_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def get_end_user_provisioning_setting_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """Get the provisioning settings available on the given site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_end_user_provisioning_setting_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The id of the site (required)
        :return: EndUserProvisioningSettingJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_end_user_provisioning_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_end_user_provisioning_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zero-touch/end-user-provisioning-settings/{siteId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EndUserProvisioningSettingJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_cisco_end_user_provisioning(self, body, **kwargs):  # noqa: E501
        """Provision a cisco end user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_cisco_end_user_provisioning(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndUserProvisioningOptionsJson body: The provisioning options (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_cisco_end_user_provisioning_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_cisco_end_user_provisioning_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_cisco_end_user_provisioning_with_http_info(self, body, **kwargs):  # noqa: E501
        """Provision a cisco end user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_cisco_end_user_provisioning_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndUserProvisioningOptionsJson body: The provisioning options (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_cisco_end_user_provisioning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_cisco_end_user_provisioning`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zero-touch/cisco/end-user-provisionings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_end_user_provisioning(self, body, **kwargs):  # noqa: E501
        """Provision an end user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_end_user_provisioning(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndUserProvisioningOptionsJson body: The provisioning options (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_end_user_provisioning_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_end_user_provisioning_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_end_user_provisioning_with_http_info(self, body, **kwargs):  # noqa: E501
        """Provision an end user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_end_user_provisioning_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndUserProvisioningOptionsJson body: The provisioning options (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_end_user_provisioning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_end_user_provisioning`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zero-touch/end-user-provisionings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
