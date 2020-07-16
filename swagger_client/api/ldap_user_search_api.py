# coding: utf-8

"""
    Helpdesk REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.8.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LdapUserSearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_ldap_users(self, **kwargs):  # noqa: E501
        """Search users via LDAP filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ldap_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: The filter to search for
        :param int max: Maximum user's number to return. If left blank, 1000 default is set. To provide no limit, set to 0.
        :return: list[LdapUserResultJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_ldap_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_ldap_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_ldap_users_with_http_info(self, **kwargs):  # noqa: E501
        """Search users via LDAP filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ldap_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: The filter to search for
        :param int max: Maximum user's number to return. If left blank, 1000 default is set. To provide no limit, set to 0.
        :return: list[LdapUserResultJson]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'max']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_ldap_users" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'max' in params:
            query_params.append(('max', params['max']))  # noqa: E501

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
            '/ldap-user-search/search-users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LdapUserResultJson]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
