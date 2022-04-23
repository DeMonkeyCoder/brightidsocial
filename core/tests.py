import json
import random

from django.urls import reverse
from rest_framework.test import APITestCase

from brightidsocial.settings import ALLOWED_HASH_COUNT
from core.consts import BrightIdNetwork
from core.models import SocialMediaVariation, SocialMedia
from initial_data.initial_social_media import upsert_initial_social_media_variations, SocialMediaVariationIds


class TestUtilsMixin:
    create_endpoint = reverse("social-media-create")
    update_endpoint = reverse("social-media-update")
    delete_endpoint = reverse("social-media-delete")
    check_verification_endpoint = reverse("social-media-check-verification")
    query_endpoint = reverse("social-media-query")

    def create_social_media(self, network, variation):
        response = self.client.post(self.create_endpoint, data={
            'network': network,
            'variation': variation.pk,
            'profileHashes': [
                '96fc9552cde1e133bd039e6b70d5aa09',
            ]
        })
        return response

    def assert_valid_social_media_create_response(self, response, network, variation):
        self.assertEqual(response.status_code, 201)
        res = json.loads(response.content)
        self.assertIsNotNone(res.get('contextId'))
        self.assertIsNotNone(res.get('token'))
        self.assertEqual(res.get('variation'), str(variation.id))
        self.assertEqual(res.get('network'), network)

    @staticmethod
    def extract_social_media_object_and_token_from_create_response(create_response):
        create_response_content = json.loads(create_response.content)
        social_media = SocialMedia.objects.get(id=create_response_content.get('contextId'))
        token = create_response_content.get('token')
        return social_media, token

    @staticmethod
    def generate_random_hash():
        return "%032x" % random.getrandbits(128)


class ListSocialMediaVariationsV1(APITestCase, TestUtilsMixin):

    @classmethod
    def setUpTestData(cls):
        upsert_initial_social_media_variations()

    def test_list_variations(self):
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.DISCORD)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.INSTAGRAM)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.KEYBASE)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.LINKEDIN)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.MEDIUM)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.REDDIT)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.SIGNAL)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.TELEGRAM)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.TWITTER)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.WHATSAPP)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.PHONE_NUMBER)
        SocialMediaVariation.objects.get(id=SocialMediaVariationIds.EMAIL)


class CreateSocialMediaV1(APITestCase, TestUtilsMixin):

    @classmethod
    def setUpTestData(cls):
        upsert_initial_social_media_variations()

    def test_create_social_media(self):
        variation = SocialMediaVariation.objects.get(id=SocialMediaVariationIds.TELEGRAM)
        network = BrightIdNetwork.NODE
        response = self.create_social_media(network, variation)
        self.assert_valid_social_media_create_response(response, network, variation)

    def test_create_test_network_social_media(self):
        variation = SocialMediaVariation.objects.get(id=SocialMediaVariationIds.PHONE_NUMBER)
        network = BrightIdNetwork.TEST
        response = self.create_social_media(network, variation)
        self.assert_valid_social_media_create_response(response, network, variation)

    def test_cannot_create_social_media_with_more_than_allowed_hashes(self):
        variation = SocialMediaVariation.objects.get(id=SocialMediaVariationIds.PHONE_NUMBER)
        network = BrightIdNetwork.TEST
        response = self.client.post(self.create_endpoint, data={
            'network': network,
            'variation': variation.pk,
            'profileHashes': [
                self.generate_random_hash() for x in range(ALLOWED_HASH_COUNT + 1)
            ]
        })
        self.assertEqual(response.status_code, 400)


class UpdateSocialMediaV1(APITestCase, TestUtilsMixin):

    @classmethod
    def setUpTestData(cls):
        upsert_initial_social_media_variations()

    def update_social_media(self, token, profile_hashes):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.put(self.update_endpoint, data={
            'profileHashes': profile_hashes
        })
        return response

    def assert_valid_social_media_update_response(self, response, social_media, new_profile_hashes):
        self.assertEqual(response.status_code, 200)
        profile_hashes = list(social_media.profile_hashes.values_list('value', flat=True))
        self.assertEqual(profile_hashes, new_profile_hashes)

    def test_update_social_media(self):
        variation = SocialMediaVariation.objects.get(id=SocialMediaVariationIds.TELEGRAM)
        network = BrightIdNetwork.NODE
        create_response = self.create_social_media(network, variation)
        new_profile_hashes = [
            '2160ec425e3344ba53f867fde461e6ee',
            '500cd23b415cd92421b5272ddc40b910',
            'a9fe4b4f3d0b4a885831ebbbee592a4d'
        ]
        social_media, token = self.extract_social_media_object_and_token_from_create_response(create_response)
        update_response = self.update_social_media(token, new_profile_hashes)
        self.assert_valid_social_media_update_response(update_response, social_media, new_profile_hashes)

    def test_cannot_update_social_media_with_more_than_allowed_hashes(self):
        variation = SocialMediaVariation.objects.get(id=SocialMediaVariationIds.TELEGRAM)
        network = BrightIdNetwork.NODE
        create_response = self.create_social_media(network, variation)
        _, token = self.extract_social_media_object_and_token_from_create_response(create_response)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.put(self.update_endpoint, data={
            'profileHashes': [
                self.generate_random_hash() for x in range(ALLOWED_HASH_COUNT + 1)
            ]
        })
        self.assertEqual(response.status_code, 400)


class DeleteSocialMediaV1(APITestCase, TestUtilsMixin):

    @classmethod
    def setUpTestData(cls):
        upsert_initial_social_media_variations()

    def delete_social_media(self, token):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.delete(self.delete_endpoint)
        return response

    def assert_valid_social_media_delete_response(self, response):
        self.assertEqual(response.status_code, 204)

    def test_delete_social_media(self):
        variation = SocialMediaVariation.objects.get(id=SocialMediaVariationIds.TELEGRAM)
        network = BrightIdNetwork.NODE
        create_response = self.create_social_media(network, variation)

        _, token = self.extract_social_media_object_and_token_from_create_response(create_response)
        delete_response = self.delete_social_media(token)
        self.assert_valid_social_media_delete_response(delete_response)
