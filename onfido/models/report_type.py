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


class ReportType(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, variant=None, options=None):
        """
        ReportType - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'variant': 'str',
            'options': 'list[ReportTypeOption]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'variant': 'variant',
            'options': 'options'
        }

        self._id = id
        self._name = name
        self._variant = variant
        self._options = options


    @property
    def id(self):
        """
        Gets the id of this ReportType.


        :return: The id of this ReportType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReportType.


        :param id: The id of this ReportType.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ReportType.


        :return: The name of this ReportType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportType.


        :param name: The name of this ReportType.
        :type: str
        """

        self._name = name

    @property
    def variant(self):
        """
        Gets the variant of this ReportType.


        :return: The variant of this ReportType.
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """
        Sets the variant of this ReportType.


        :param variant: The variant of this ReportType.
        :type: str
        """

        self._variant = variant

    @property
    def options(self):
        """
        Gets the options of this ReportType.


        :return: The options of this ReportType.
        :rtype: list[ReportTypeOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this ReportType.


        :param options: The options of this ReportType.
        :type: list[ReportTypeOption]
        """

        self._options = options

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
