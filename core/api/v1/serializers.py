import uuid

from django.contrib.auth.models import User
from rest_framework import serializers

from core.consts import BrightIdNetwork
from core.models import SocialMedia, SocialMediaVariation


class SocialMediaVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaVariation
        fields = (
            'id',
            'name',
            'icon',
            'type',
            'share_type',
            'share_type_display',
            'share_action_type',
            'share_action_data_format',
            'bright_id_app_name',
        )


class SocialMediaCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = (
            'context_id',
            'token',
            'network',
            'variation',
            'profile',
        )

    def create(self, validated_data):
        django_user = User.objects.create_user(
            # random, with no purpose
            username=uuid.uuid4().hex[:30]
        )
        social_media = SocialMedia.objects.create(
            **validated_data,
            django_user=django_user
        )
        return social_media


class SocialMediaVerifySerializer(serializers.Serializer):
    context_id = serializers.UUIDField()
    network = serializers.ChoiceField(
        choices=BrightIdNetwork.choices,
    )
