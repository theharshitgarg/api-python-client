# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit background checking requests

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Check(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, href=None, type=None, status=None, tags=None, result=None, download_uri=None, form_uri=None, redirect_uri=None, results_uri=None, reports=None):
        """
        Check - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'created_at': 'datetime',
            'href': 'str',
            'type': 'str',
            'status': 'str',
            'tags': 'list[str]',
            'result': 'str',
            'download_uri': 'str',
            'form_uri': 'str',
            'redirect_uri': 'str',
            'results_uri': 'str',
            'reports': 'list[object]'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'href': 'href',
            'type': 'type',
            'status': 'status',
            'tags': 'tags',
            'result': 'result',
            'download_uri': 'download_uri',
            'form_uri': 'form_uri',
            'redirect_uri': 'redirect_uri',
            'results_uri': 'results_uri',
            'reports': 'reports'
        }

        self._id = id
        self._created_at = created_at
        self._href = href
        self._type = type
        self._status = status
        self._tags = tags
        self._result = result
        self._download_uri = download_uri
        self._form_uri = form_uri
        self._redirect_uri = redirect_uri
        self._results_uri = results_uri
        self._reports = reports


    @property
    def id(self):
        """
        Gets the id of this Check.


        :return: The id of this Check.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Check.


        :param id: The id of this Check.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Check.
        The date and time when this check was created.

        :return: The created_at of this Check.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Check.
        The date and time when this check was created.

        :param created_at: The created_at of this Check.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def href(self):
        """
        Gets the href of this Check.
        The uri of this resource.

        :return: The href of this Check.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this Check.
        The uri of this resource.

        :param href: The href of this Check.
        :type: str
        """

        self._href = href

    @property
    def type(self):
        """
        Gets the type of this Check.
        The type of the check: standard or express.

        :return: The type of this Check.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Check.
        The type of the check: standard or express.

        :param type: The type of this Check.
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """
        Gets the status of this Check.
        The current state of the check in the checking process.

        :return: The status of this Check.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Check.
        The current state of the check in the checking process.

        :param status: The status of this Check.
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """
        Gets the tags of this Check.
        A list of tags associated with this check.

        :return: The tags of this Check.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Check.
        A list of tags associated with this check.

        :param tags: The tags of this Check.
        :type: list[str]
        """

        self._tags = tags

    @property
    def result(self):
        """
        Gets the result of this Check.
        The overall result of the check, based on the results of the constituent reports.

        :return: The result of this Check.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this Check.
        The overall result of the check, based on the results of the constituent reports.

        :param result: The result of this Check.
        :type: str
        """

        self._result = result

    @property
    def download_uri(self):
        """
        Gets the download_uri of this Check.


        :return: The download_uri of this Check.
        :rtype: str
        """
        return self._download_uri

    @download_uri.setter
    def download_uri(self, download_uri):
        """
        Sets the download_uri of this Check.


        :param download_uri: The download_uri of this Check.
        :type: str
        """

        self._download_uri = download_uri

    @property
    def form_uri(self):
        """
        Gets the form_uri of this Check.


        :return: The form_uri of this Check.
        :rtype: str
        """
        return self._form_uri

    @form_uri.setter
    def form_uri(self, form_uri):
        """
        Sets the form_uri of this Check.


        :param form_uri: The form_uri of this Check.
        :type: str
        """

        self._form_uri = form_uri

    @property
    def redirect_uri(self):
        """
        Gets the redirect_uri of this Check.


        :return: The redirect_uri of this Check.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this Check.


        :param redirect_uri: The redirect_uri of this Check.
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def results_uri(self):
        """
        Gets the results_uri of this Check.


        :return: The results_uri of this Check.
        :rtype: str
        """
        return self._results_uri

    @results_uri.setter
    def results_uri(self, results_uri):
        """
        Sets the results_uri of this Check.


        :param results_uri: The results_uri of this Check.
        :type: str
        """

        self._results_uri = results_uri

    @property
    def reports(self):
        """
        Gets the reports of this Check.


        :return: The reports of this Check.
        :rtype: list[object]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """
        Sets the reports of this Check.


        :param reports: The reports of this Check.
        :type: list[object]
        """

        self._reports = reports

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
