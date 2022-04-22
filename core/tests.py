import json

from django.urls import reverse
from rest_framework.test import APITestCase

from core.consts import BrightIdNetwork
from core.models import SocialMediaVariation
from initial_data.initial_social_media import upsert_initial_social_media_variations, SocialMediaVariationIds


class TestSocialMediaV1(APITestCase):

    @classmethod
    def setUpTestData(cls):
        upsert_initial_social_media_variations()

    def test_are_variations_loaded(self):
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

    def create_social_media(self, network, variation):
        endpoint = reverse("social-media-create")
        response = self.client.post(endpoint, data={
            'network': network,
            'variation': variation.pk,
            'profileHashes': [
                '96fc9552cde1e133bd039e6b70d5aa09',
                '257ac821a45283846712708b733233e6',
                '642fe2bcdced2067e1fc7b5c4835f524'
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

    def test_cannot_create_social_media_with_more_than_three_hashes(self):
        variation = SocialMediaVariation.objects.get(id=SocialMediaVariationIds.PHONE_NUMBER)
        network = BrightIdNetwork.TEST
        endpoint = reverse("social-media-create")
        response = self.client.post(endpoint, data={
            'network': network,
            'variation': variation.pk,
            'profileHashes': [
                '96fc9552cde1e133bd039e6b70d5aa09',
                '257ac821a45283846712708b733233e6',
                '642fe2bcdced2067e1fc7b5c4835f524',
                '8b6d15200eb17f1468d4bd10ac0434a0'
            ]
        })
        self.assertEqual(response.status_code, 400)