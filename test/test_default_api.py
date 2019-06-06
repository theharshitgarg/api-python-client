# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onfido
from onfido.api.default_api import DefaultApi  # noqa: E501
from onfido.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = onfido.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_report(self):
        """Test case for cancel_report

        This endpoint is for cancelling individual paused reports.  # noqa: E501
        """
        pass

    def test_create_applicant(self):
        """Test case for create_applicant

        Create Applicant  # noqa: E501
        """
        pass

    def test_create_check(self):
        """Test case for create_check

        Create a check  # noqa: E501
        """
        pass

    def test_create_webhook(self):
        """Test case for create_webhook

        Create a webhook  # noqa: E501
        """
        pass

    def test_delete_webhook(self):
        """Test case for delete_webhook

        Delete a webhook  # noqa: E501
        """
        pass

    def test_destroy_applicant(self):
        """Test case for destroy_applicant

        Delete Applicant  # noqa: E501
        """
        pass

    def test_download_document(self):
        """Test case for download_document

        Download a documents raw data  # noqa: E501
        """
        pass

    def test_download_live_photo(self):
        """Test case for download_live_photo

        Download live photo  # noqa: E501
        """
        pass

    def test_download_live_video(self):
        """Test case for download_live_video

        Download live video  # noqa: E501
        """
        pass

    def test_edit_webhook(self):
        """Test case for edit_webhook

        Edit a webhook  # noqa: E501
        """
        pass

    def test_find_addresses(self):
        """Test case for find_addresses

        Search for addresses by postcode  # noqa: E501
        """
        pass

    def test_find_applicant(self):
        """Test case for find_applicant

        Retrieve Applicant  # noqa: E501
        """
        pass

    def test_find_check(self):
        """Test case for find_check

        Retrieve a Check  # noqa: E501
        """
        pass

    def test_find_document(self):
        """Test case for find_document

        A single document can be retrieved by calling this endpoint with the document’s unique identifier.  # noqa: E501
        """
        pass

    def test_find_live_photo(self):
        """Test case for find_live_photo

        Retrieve live photo  # noqa: E501
        """
        pass

    def test_find_live_video(self):
        """Test case for find_live_video

        Retrieve live video  # noqa: E501
        """
        pass

    def test_find_report(self):
        """Test case for find_report

        A single report can be retrieved using this endpoint with the corresponding unique identifier.  # noqa: E501
        """
        pass

    def test_find_report_type_group(self):
        """Test case for find_report_type_group

        Retrieve single report type group object  # noqa: E501
        """
        pass

    def test_find_webhook(self):
        """Test case for find_webhook

        Retrieve a Webhook  # noqa: E501
        """
        pass

    def test_generate_sdk_token(self):
        """Test case for generate_sdk_token

        Generate a SDK token  # noqa: E501
        """
        pass

    def test_list_applicants(self):
        """Test case for list_applicants

        List Applicants  # noqa: E501
        """
        pass

    def test_list_checks(self):
        """Test case for list_checks

        Retrieve Checks  # noqa: E501
        """
        pass

    def test_list_documents(self):
        """Test case for list_documents

        List documents  # noqa: E501
        """
        pass

    def test_list_live_photos(self):
        """Test case for list_live_photos

        List live photos  # noqa: E501
        """
        pass

    def test_list_live_videos(self):
        """Test case for list_live_videos

        List live videos  # noqa: E501
        """
        pass

    def test_list_report_type_groups(self):
        """Test case for list_report_type_groups

        Retrieve all report type groups  # noqa: E501
        """
        pass

    def test_list_reports(self):
        """Test case for list_reports

        All the reports belonging to a particular check can be listed from this endpoint.  # noqa: E501
        """
        pass

    def test_list_webhooks(self):
        """Test case for list_webhooks

        List webhooks  # noqa: E501
        """
        pass

    def test_restore_applicant(self):
        """Test case for restore_applicant

        Restore Applicant  # noqa: E501
        """
        pass

    def test_resume_check(self):
        """Test case for resume_check

        Resume a Check  # noqa: E501
        """
        pass

    def test_resume_report(self):
        """Test case for resume_report

        This endpoint is for resuming individual paused reports.  # noqa: E501
        """
        pass

    def test_update_applicant(self):
        """Test case for update_applicant

        Update Applicant  # noqa: E501
        """
        pass

    def test_upload_document(self):
        """Test case for upload_document

        Upload a document  # noqa: E501
        """
        pass

    def test_upload_live_photo(self):
        """Test case for upload_live_photo

        Upload live photo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
